import numpy as np
import openai
from modules.rag.vectorstore import load_vectorstore


def embed_query(query):
    response = openai.embeddings.create(
        input=[query],
        model="text-embedding-ada-002"
    )
    return np.array(response.data[0].embedding).astype("float32")


def retrieve_relevant_chunks(query, k=5):
    query_vec = embed_query(query)
    index, texts = load_vectorstore()

    D, I = index.search(np.array([query_vec]), k)  # distances and indices
    matches = [texts[i] for i in I[0]]

    print(f"🔎 Top {k} results for: \"{query}\"")
    return matches