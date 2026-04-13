## 👤 Candidate Information

| **Field** | **Details** |
|----------|-------------|
| **Name** | Sudalai Eswari S |
| **Dept** | Information Technology |
| **Institution** | V.S.B Engineering College, Karur |
| **Email** | ssudalaieswari@gmail.com |
| **GitHub** |https://github.com/SudalaiEswari|
| **Project** | CodeMentor AI - Intelligent Coding Assistant |

# CodeMentor AI Assistant

A premium AI-powered coding assistant built using Next.js 14 and FastAPI, leveraging the Endee Vector Database to implement Retrieval-Augmented Generation (RAG) for context-aware and accurate coding assistance.

##  Prerequisites
* Docker (for Endee Vector Database)
* Python 3.10+ (Backend)
* Node.js 18+ (Frontend)
* Google Gemini API Key (configured in .env)
## ⚙️ How It Works
 1. Knowledge Ingestion
The system accepts user-provided data such as:
 * Coding notes
 * Project files
 * Documentation
 * Problem statements

## Processing Steps:
* Parse input data
* Split into meaningful chunks
* Generate embeddings
* Store in Endee with metadata
Example Path: C:\Users\Admin\Projects\CodeMentor\data

## 2. Semantic Retrieval
When a user submits a query:
 * Query is converted into embeddings
 * Endee retrieves relevant data
 * Uses vector similarity search
## 3. AI Response Generation (RAG)
Retrieved context is sent to Gemini API
AI generates:
* Explanation
* Code solutions
* Debugging assistance
## Why Endee?
* ⚡ High-performance vector search
* 🧩 Metadata filtering support
* 📈 Scalable architecture
* 🧠 Accurate semantic understanding
Endee acts as the knowledge backbone of the system.

 ## 🚀 Getting Started
1. Start Vector Database
docker compose up -d

Available at: http://localhost:8080

2. Start Backend (FastAPI)
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload

API: http://localhost:8000

3. Start Frontend (Next.js)
cd frontend
npm install
npm run dev

UI: http://localhost:3000

🧪 Usage
1️⃣ Ingest Data
Upload:

* Project code
* Notes
* PDFs
The system indexes data into Endee.

2️⃣ Ask Questions

Examples:
* “Explain Java loops simply”
* “Fix null pointer exception”
* “Provide optimized sorting algorithm”

3️⃣ Get AI Responses
Each response includes:
* 💡 Explanation
* 🧩 Code snippet
* ⚡ Optimized solution

## Sample Queries
* “Explain OOP concepts in Java”
* “Fix this API error”
* “Give DSA interview questions”
* “Explain this code line by line”
## Features
* Glassmorphic UI – Modern and visually appealing interface
* RAG Integration – Context-aware responses using Endee
* Gemini Powered – Fast and accurate AI responses
## Screenshot
<img width="1920" height="1080" alt="CodeMentor UI" src="https://github.com/user-attachments/assets/e5aa44ad-8fd5-4748-8304-f70c36e8b1f3" />
