from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

def load_vectorstore(persist_path="faiss_index"):
    if os.path.exists(persist_path):
        return FAISS.load_local(persist_path, HuggingFaceEmbeddings(), allow_dangerous_deserialization=True)

    loaders = [PyPDFLoader(f"documents/{file}") for file in os.listdir("documents") if file.endswith(".pdf")]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(split_docs, embeddings)
    db.save_local(persist_path)
    return db
