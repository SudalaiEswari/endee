import os
import google.generativeai as genai
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-flash-latest')
        self.embedding_model = "models/gemini-embedding-001"

    async def get_embedding(self, text: str) -> List[float]:
        try:
            result = genai.embed_content(
                model=self.embedding_model,
                content=text,
                task_type="retrieval_document"
            )
            return result['embedding']
        except Exception as e:
            print(f"Embedding Error: {e}")
            return []

    async def generate_response(self, prompt: str, history: Optional[List] = None) -> str:
        try:
            chat = self.model.start_chat(history=history or [])
            response = chat.send_message(prompt)
            return response.text
        except Exception as e:
            print(f"Generation Error: {e}")
            return f"Error: {str(e)}"

llm_service = GeminiService()
