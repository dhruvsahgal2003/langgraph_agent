from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("AIzaSyDPh4yh36JuWPJRECWTVoYh72EvNOExK8k")

def get_qa_chain_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents, embeddings)

    from langchain_google_genai import ChatGoogleGenerativeAI

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash",
        google_api_key="AIzaSyDPh4yh36JuWPJRECWTVoYh72EvNOExK8k",
        convert_system_message_to_human=True  # optional, helps in some formats
    )

    # 🔥 This line is the key: change input_key="query" → "question"
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
        input_key="question"  # ✅ match FastAPI input key
    )

    return qa_chain
