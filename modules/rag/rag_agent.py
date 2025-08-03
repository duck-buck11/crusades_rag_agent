from modules.rag.loader import load_documents
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI

def ingest_and_index():
    # Load documents from S3
    docs: list[Document] = load_documents()
    print(f"Loaded {len(docs)} document(s)")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    splits = splitter.split_documents(docs)
    print(f"Split into {len(splits)} chunks")

    # Embed and index in FAISS
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local("faiss_index")
    print("FAISS index saved locally")

def answer_query(query: str) -> str:
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        retriever=retriever
    )

    result = qa_chain.run(query)
    return result