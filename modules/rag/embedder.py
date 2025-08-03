from langchain_openai import OpenAIEmbeddings


def get_embeddings():
    """
    Initializes the OpenAI embedding model.
    """
    return OpenAIEmbeddings(model="text-embedding-3-small")  # cheaper for dev


def embed_documents(documents, embedder):
    """
    Generates vector embeddings for each document chunk.
    """
    texts = [doc.page_content for doc in documents]
    print(f"🧠 Embedding {len(texts)} documents...")
    embeddings = embedder.embed_documents(texts)
    print("✅ Embedding complete.")
    return embeddings, texts