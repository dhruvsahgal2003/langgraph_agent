from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

def get_qa_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa
