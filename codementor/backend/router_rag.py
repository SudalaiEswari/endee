from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.llm import llm_service
from services.endee_client import endee_client
import os

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        # 1. Get embedding and context (with fallback)
        context = ""
        results = []
        try:
            if os.getenv("MOCK_MODE", "False").lower() != "true":
                query_vector = await llm_service.get_embedding(request.message)
                index_name = os.getenv("ENDEE_INDEX", "codementor_knowledge")
                results = await endee_client.search(index_name, query_vector, top_k=3)
                if results:
                    context = "\n".join([r.get("meta", {}).get("text", "") for r in results])
        except Exception as e:
            print(f"Endee Search Error (Falling back to default chat): {e}")

        
        # 3. Construct prompt with context
        system_prompt = "You are CodeMentor, an expert AI programming assistant. Use the following context to answer the user request precisely."
        if context:
            prompt = f"{system_prompt}\n\nContext:\n{context}\n\nUser: {request.message}"
        else:
            prompt = f"{system_prompt}\n\nUser: {request.message}"
            
        # 4. Generate response from Gemini
        response = await llm_service.generate_response(prompt)
        
        return {
            "response": response,
            "context_retrieved": len(results) > 0
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
