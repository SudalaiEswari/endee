import httpx
import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

class EndeeClient:
    def __init__(self):
        self.base_url = os.getenv("ENDEE_URL", "http://localhost:8080")
        if not self.base_url.endswith("/api/v1"):
            self.base_url += "/api/v1"
        self.auth_token = os.getenv("ENDEE_TOKEN")

    async def get_headers(self):
        headers = {"Content-Type": "application/json"}
        if self.auth_token:
            headers["Authorization"] = self.auth_token
        return headers

    async def create_index(self, name: str, dimension: int = 3072):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{self.base_url}/index/create",
                json={"name": name, "dimension": dimension, "sparse": False},
                headers=await self.get_headers()
            )
            return resp.json()

    async def upsert(self, index_name: str, items: List[Dict[str, Any]]):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{self.base_url}/index/{index_name}/upsert",
                json={"items": items},
                headers=await self.get_headers()
            )
            return resp.json()

    async def search(self, index_name: str, vector: List[float], top_k: int = 5):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{self.base_url}/index/{index_name}/search",
                json={"vector": vector, "limit": top_k},
                headers=await self.get_headers()
            )
            if resp.status_code != 200:
                print(f"Endee Search Error: {resp.text}")
                return []
            return resp.json().get("results", [])

endee_client = EndeeClient()
