from dotenv import load_dotenv
from mem0 import Memory
import os
from google import genai
import json

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Gemini client with API key
client = genai.Client(api_key=GEMINI_API_KEY)

# ✅ mem0 configuration
config = {
    "version": "v1.1",
    "embedder": {
        "provider": "gemini",
        "config": {
            # Local embedding model (no API key required)
            "model": "gemini-embedding-001",
             "output_dimensionality": 1536    
        }
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "gemini-2.5-flash",
               
        }
    },
    
    "graph_store":{
        "provider": "neo4j",
        "config": {
            "url": "neo4j+s://24088203.databases.neo4j.io",
            "username": "neo4j",
            "password": "XfprNCGfvNfp6eGup7Krz3kYBdWndOp74UZNEHWG_o0"
        }
    },
    
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "collection_name": "mem_agent_conversations",
            "embedding_model_dims": 1536  
        }
    }
}

# ✅ Initialize memory
mem_client = Memory.from_config(config)


while True:


    # User input
    user_query = input("> ")

    search_memory = mem_client.search(query=user_query, user_id="Ravi Yadav")
    
    Memory_about_user = search_memory

    memories = [
        f"ID: {mem.get('id')}\nMemory: {mem.get('Memory')}"  for mem in search_memory.get("results")
    ]

    print("Found Memories", memories)

    SYSTEM_PROMPT = """
        Here is the context about the user:
        {json.dumps(memories)}
    """

    # Generate Gemini response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {
                "role": "system",
                "parts": [{"text": SYSTEM_PROMPT}],
                "role": "user",
                "parts": [{"text": user_query}]
            }
        ]
    )

    ai_response = response.text
    print("AI:", ai_response)

    # ✅ Store conversation in memory
    mem_client.add(
        user_id="Ravi Yadav",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

    print("✅ Memory has been saved")




