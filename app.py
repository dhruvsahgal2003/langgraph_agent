from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os

from chatbot import get_qa_chain_from_pdf

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Upload directory
UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Global chain
qa_chain = None

# Request model
class Question(BaseModel):
    question: str  # <-- Rename this to match what the chain expects

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global qa_chain

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        qa_chain = get_qa_chain_from_pdf(file_path)
        return {"message": f"{file.filename} uploaded and processed"}
    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}

@app.post("/ask")
async def ask_question(payload: Question):
    global qa_chain
    if qa_chain is None:
        return {"error": "No document uploaded yet"}

    try:
        response = qa_chain.invoke({"question": payload.question})
        return {"answer": response}
    except Exception as e:
        return {"error": f"Failed to answer query: {str(e)}"}
