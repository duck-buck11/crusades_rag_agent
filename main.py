from modules.rag.rag_agent import ingest_and_index, answer_query

def main():
    # Step 1: Ingest and build index (only needs to be done once)
    ingest_and_index()

    # Step 2: Ask a question
    query = "What was the cause of the First Crusade?"
    result = answer_query(query)
    print("Answer:", result)

if __name__ == "__main__":
    main()