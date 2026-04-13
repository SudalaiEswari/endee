# CodeMentor AI Assistant

A premium, AI-powered coding assistant built with Next.js 14 and FastAPI, leveraging the Endee Vector Database for context-aware RAG (Retrieval-Augmented Generation).

## Prerequisites
- **Docker** (to run Endee Vector Database)
- **Python 3.10+** (for the backend)
- **Node.js 18+** (for the frontend)
- **Google Gemini API Key** (already configured in `.env`)

## Getting Started

### 1. Start Vector Database
```bash
docker compose up -d
```
The database will be available at `http://localhost:8080`.

### 2. Start Backend (FastAPI)
```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

### 3. Start Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```
The UI will be available at `http://localhost:3000`.

## Features
- **Glassmorphic UI**: Premium aesthetic with blur effects and sleek typography.
- **RAG Integration**: Retrieves context from Endee for precise coding advice.
- **Gemini Powered**: Uses `gemini-1.5-flash` for fast and accurate responses.
