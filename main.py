from modules.rag.loader import load_documents

def main():
    print("Loading documents from S3...")
    docs = load_documents(bucket="crusades-rag-data-s3", prefix="")  # customize prefix if needed
    print(f"✅ Loaded {len(docs)} document(s)\n")

    for i, doc in enumerate(docs[:5]):  # show a sample
        print(f"--- Document {i+1} ---")
        print(doc.page_content[:300])  # show first 300 chars
        print("\n")

if __name__ == "__main__":
    main()