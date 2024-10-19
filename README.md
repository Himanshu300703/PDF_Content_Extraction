<<<<<<< HEAD
# rishi-pawar-wasserstoff-AiInternTask
# PDF Processing Pipeline

## Overview
This project implements a PDF processing pipeline that ingests PDF documents, extracts metadata, summarizes the content, performs keyword extraction, and stores the results in a MongoDB database. 

## Features
- **PDF Ingestion**: Downloads and processes PDF files from a specified directory.
- **Summarization**: Generates summaries of the extracted text using Natural Language Processing (NLP).
- **Keyword Extraction**: Extracts keywords from the text using the RAKE algorithm.
- **MongoDB Integration**: Stores metadata, summaries, and keywords in a MongoDB database.

## Project Structure
project_name/
│
├── data/
│   ├── pdf_links.json  
│
├── src/
│   ├── __init__.py       
│   ├── pdf_ingestion.py  
│   ├── summarization.py  
│   ├── keyword_extraction.py  
│   ├── mongodb_handler.py  
│   └── concurrency.py     
│
├── logs/
│   └── error_log.txt     
│
├── tests/
│   └── test_pipeline.py   
│
├── Dockerfile             
│
├── README.md        
│
└── main.py          


## Installation
1. Clone the repository:

   git clone https://github.com/Himanshu300703/rishi-pawar-wasserstoff-AiInternTask
   
   cd your_project_name
   
   Ensure MongoDB is installed and running. Update your MongoDB connection string in the mongodb_handler.py file.

## Run

1.  Install Dependencies
   
    ~pip install -r requirements.txt

2. ~python src/pdf_ingestion.py

## View summarization results (summarization, metadata, size, path)

1. Open cmd 

    ~mongosh

2. Copy the connection string and edit in mongodb_handler.py

3. ~show dbs

4. ~use pdf_summaries_db

5. ~db.pdf_documents.find().pretty()
=======
# Himanshu300703-rishi-pawar-wasserstoff-AiInternTask
>>>>>>> 014242aebd156be9989eb8072afc1e9704353940
