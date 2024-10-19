import os
import concurrent.futures
from pdf_ingestion import process_pdf 
from pymongo import MongoClient
import logging

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PDF_FOLDER_PATH = 'data/downloaded_pdfs'

# MongoDB connection
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2')
db = client['pdf_summarization']
collection = db['pdf_metadata']

def process_single_pdf(pdf_file):
    """
    to process a single PDF, including summarizing and extracting keywords, 
    and store metadata in MongoDB.
    """
    try:
        pdf_path = os.path.join(PDF_FOLDER_PATH, pdf_file)
        
        metadata, summary, keywords = process_pdf(pdf_path)
       
        if metadata:
            metadata['summary'] = summary
            metadata['keywords'] = keywords
            collection.insert_one(metadata)
            logger.info(f"Inserted metadata for {pdf_file} into MongoDB with ID: {metadata['_id']}")
        
        return pdf_file, metadata, summary, keywords
    except Exception as e:
        logger.error(f"Error processing {pdf_file}: {e}")
        return pdf_file, None, None, None


def process_pdfs_concurrently():
    """
    to process all PDFs concurrently using ThreadPoolExecutor.
    """
    pdf_files = [f for f in os.listdir(PDF_FOLDER_PATH) if f.endswith('.pdf')]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # map the process_single_pdf function to all PDF files
        results = list(executor.map(process_single_pdf, pdf_files))

    for pdf_file, metadata, summary, keywords in results:
        if metadata is not None:
            logger.info(f"Processed {pdf_file} successfully.")
        else:
            logger.error(f"Failed to process {pdf_file}")

if __name__ == "__main__":
    process_pdfs_concurrently()
