import os
import requests
import PyPDF2
import json
import concurrent.futures
from summarization import summarize_text
from keyword_extraction import extract_keywords
from mongodb_handler import store_pdf_metadata, update_pdf_summary_and_keywords

PDF_DIR = 'data/downloaded_pdfs'
os.makedirs(PDF_DIR, exist_ok=True)

import certifi

# to download PDFs from the URLs
def download_pdf(url, filename):
    try:
        response = requests.get(url, verify=certifi.where())
        if response.status_code == 200:
            pdf_path = os.path.join(PDF_DIR, filename)
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
            return pdf_path
        else:
            print(f"Failed to download {filename}")
            return None
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
        return None

# to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
            return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

# to get PDF metadata
def get_pdf_metadata(pdf_path):
    try:
        size = os.path.getsize(pdf_path)  # Get file size in bytes
        return {
            "document_name": os.path.basename(pdf_path),
            "path": pdf_path,
            "size": size
        }
    except Exception as e:
        print(f"Error getting metadata for {pdf_path}: {e}")
        return None

# to process a single PDF from a URL
def process_pdf(pdf_path):
    # metadata
    metadata = get_pdf_metadata(pdf_path)
    
    # store metadata in MongoDB
    store_pdf_metadata(metadata)

    # extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    if text:
        summary = summarize_text(text, num_sentences=3)
        
        keywords = extract_keywords(text, max_keywords=5)
        
        # update MongoDB with summary and keywords
        update_pdf_summary_and_keywords(metadata['document_name'], summary, keywords)

# to read the JSON file containing PDF URLs
def read_pdf_links(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return {}

# concurrently process PDFs using ThreadPoolExecutor
def process_all_pdfs_concurrently():
    pdf_paths = [os.path.join(PDF_DIR, filename) for filename in os.listdir(PDF_DIR)]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_pdf, pdf_path) for pdf_path in pdf_paths]
        
        # Waiting for all tasks to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing PDF: {e}")

if __name__ == "__main__":
    process_all_pdfs_concurrently()
