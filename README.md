# LangGraph Agent

LangGraph Agent is a lightweight FastAPI application that lets you upload PDF files and ask questions based on their content using a local embedding model (via HuggingFace) and Google Gemini for intelligent response generation.

## 🚀 Features

- 📄 Upload a PDF document
- 🤖 Ask questions based on the uploaded document
- 🔍 Uses FAISS + Sentence Transformers for vector storage
- 🧠 Uses Gemini Pro (via LangChain) for answer generation
- ⚡ Built with FastAPI + LangChain
- 🌐 Exposable via Ngrok for easy sharing

---

## 📁 Project Structure

langgraph_agent/
├── app.py # FastAPI app with endpoints for upload and query
├── chatbot.py # PDF loading, embedding, vectorstore, and chain logic
├── vectorstore.py # Utility to persist/load FAISS vectorstore
├── uploaded_docs/ # Directory to save uploaded PDFs
├── requirements.txt # Dependencies
└── README.md # You’re here


---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/dhruvsahgal2003/langgraph_agent.git
cd langgraph_agent
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Set your Google API Key
export GOOGLE_API_KEY=your_api_key_here
🔐 You can also add this to a .env file and use python-dotenv.
5. Run the App
uvicorn app:app --reload
6. Test it with Swagger UI
Visit: http://localhost:8000/docs

🌍 Expose via Ngrok (Optional)

ngrok http 8000
Then use the Ngrok URL in your frontend or cURL calls.

🧪 API Endpoints

POST /upload
Uploads a PDF to the server and prepares it for question answering.

Body: multipart/form-data

Field	Type	Description
file	PDF	The PDF to upload
POST /ask
Asks a question based on the uploaded PDF.

Body: application/json

{
  "question": "What is this document about?"
}
✅ To-Do

 Add multi-file support
 Add user sessions or persistent chat history
 Add a frontend for easy use
📜 License

MIT © Dhruv Sahgal

