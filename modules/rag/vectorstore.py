import faiss
import pickle
import os
import numpy as np


def save_vectorstore(embeddings, texts, path="vectorstore"):
    """
    Save FAISS index and associated texts to disk.
    """
    os.makedirs(path, exist_ok=True)

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, os.path.join(path, "index.faiss"))

    with open(os.path.join(path, "texts.pkl"), "wb") as f:
        pickle.dump(texts, f)

    print(f"💾 Saved FAISS index and {len(texts)} texts to {path}/")


def load_vectorstore(path="vectorstore"):
    """
    Load FAISS index and associated texts from disk.
    """
    index_path = os.path.join(path, "index.faiss")
    texts_path = os.path.join(path, "texts.pkl")

    if not os.path.exists(index_path) or not os.path.exists(texts_path):
        raise FileNotFoundError("Missing FAISS index or text metadata")

    index = faiss.read_index(index_path)

    with open(texts_path, "rb") as f:
        texts = pickle.load(f)

    return index, texts