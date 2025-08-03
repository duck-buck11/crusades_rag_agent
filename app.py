import streamlit as st
from modules.rag.rag_agent import ingest_and_index, answer_query

st.set_page_config(page_title="Crusades RAG", layout="centered")

st.title("🛡️ Crusades Retrieval Agent")
st.markdown("Ask a question about the Crusades based on your uploaded source documents.")

# Ingest & index button
if st.button("🔄 Ingest & Index Documents"):
    with st.spinner("Loading and indexing documents..."):
        ingest_and_index()
    st.success("Documents ingested and FAISS index created!")

# Query input
query = st.text_input("Ask your question:", placeholder="e.g. What caused the First Crusade?")

if st.button("🎯 Get Answer") and query.strip():
    with st.spinner("Searching and answering..."):
        result = answer_query(query)
    st.success("✅ Answer:")
    st.write(result)