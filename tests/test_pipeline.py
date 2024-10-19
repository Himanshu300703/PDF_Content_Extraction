import unittest
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/himan/Desktop/Wasserstoff_23'))
sys.path.append(project_root)

from src.pdf_ingestion import process_pdf
from src.summarization import summarize_text
from src.keyword_extraction import extract_keywords

class TestPipeline(unittest.TestCase):
    
    def test_process_pdf(self):
        """Test processing of a sample PDF."""
        pdf_path = os.path.join(project_root, "data", "downloaded_pdfs", "pdf1.pdf")
        result = process_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertIn("text", result)
        self.assertIn("metadata", result)

    def test_summarize_text(self):
        """Test summarization functionality."""
        sample_text = "This is a test text. It should be summarized."
        summary = summarize_text(sample_text)
        self.assertGreater(len(summary), 0)

    def test_extract_keywords(self):
        """Test keyword extraction functionality."""
        sample_text = "This is a test text for keyword extraction."
        keywords = extract_keywords(sample_text)
        self.assertGreater(len(keywords), 0)

if __name__ == "__main__":
    unittest.main()
