from pymongo import MongoClient

# connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2')
db = client['pdf_summaries_db']
collection = db['pdf_documents']

# to store PDF metadata
def store_pdf_metadata(metadata):
    try:
        # insert metadata into MongoDB
        result = collection.insert_one(metadata)
        print(f"Inserted PDF metadata with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting metadata into MongoDB: {e}")

# to update PDF document with summary and keywords
def update_pdf_summary_and_keywords(document_name, summary, keywords):
    try:
        # finding document by name and update its summary and keywords
        collection.update_one(
            {"document_name": document_name},
            {"$set": {"summary": summary, "keywords": keywords}}
        )
        print(f"Updated PDF document: {document_name}")
    except Exception as e:
        print(f"Error updating document in MongoDB: {e}")

if __name__ == "__main__":
    metadata = {
        "document_name": "example.pdf",
        "path": "path/to/example.pdf",
        "size": 102400
    }
    store_pdf_metadata(metadata)
    update_pdf_summary_and_keywords("example.pdf", "This is a summary.", ["keyword1", "keyword2"])
