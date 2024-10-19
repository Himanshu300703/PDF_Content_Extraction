# __init__.py

from src.pdf_ingestion import process_pdf
from src.summarization import summarize_text
from src.keyword_extraction import extract_keywords
from src.mongodb_handler import store_pdf_metadata

__version__ = '1.0.0'
__author__ = 'Himanshu'

def describe_package():
    return "This package processes PDFs, extracts metadata, summarizes content, and stores it in MongoDB."
