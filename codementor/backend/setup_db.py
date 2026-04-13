import asyncio
import os
from services.llm import llm_service
from services.endee_client import endee_client
from dotenv import load_dotenv

load_dotenv()

# Sample Technical Knowledge to Ingest
TECHNICAL_DATA = [
    {
        "title": "FastAPI Basics",
        "text": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints."
    },
    {
        "title": "React and Next.js",
        "text": "Next.js is a React framework that gives you building blocks to create web applications. It handles routing, rendering, and more."
    },
    {
        "title": "Vector Databases & RAG",
        "text": "Retrieval-Augmented Generation (RAG) is a technique for enhancing the accuracy and reliability of generative AI models with facts fetched from external sources like Endee Vector DB."
    },
    {
        "title": "Endee Vector DB",
        "text": "Endee is a high-performance vector database designed for AI memory and RAG. It supports large-scale similarity search and metadata filtering."
    }
]

async def setup():
    index_name = os.getenv("ENDEE_INDEX", "codementor_knowledge")
    print(f"--- Initializing Endee Index: {index_name} ---")
    
    # 1. Create Index (Dimension 768 for gemini-embedding-001)
    try:
        await endee_client.create_index(index_name, dimension=768)
        print(f"Index '{index_name}' created or already exists.")
    except Exception as e:
        print(f"Index creation note: {e}")

    # 2. Generate Embeddings and Ingest
    print(f"--- Ingesting {len(TECHNICAL_DATA)} knowledge pieces ---")
    items = []
    for i, data in enumerate(TECHNICAL_DATA):
        print(f"  > Processing: {data['title']}")
        vector = await llm_service.get_embedding(data['text'])
        if vector:
            items.append({
                "id": f"kb-{i}",
                "vector": vector,
                "meta": {
                    "title": data['title'],
                    "text": data['text'],
                    "source": "initial_setup"
                }
            })
    
    if items:
        resp = await endee_client.upsert(index_name, items)
        print(f"Successfully ingested data: {resp}")
    else:
        print("Failed to generate embeddings.")

    print("\n--- Setup Complete! Your CodeMentor is now 'brain-boosted' with RAG context. ---")

if __name__ == "__main__":
    asyncio.run(setup())
