from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from google import genai

client = genai.Client(
    api_key=""
)    

# Vector Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

# Chat / Querying
user_query = input("Ask Something:")

# Relevent chunks from the vector db
search_results = vector_db.similarity_search(
    query=user_query
)

context = "\n\n\n".join([f"Page Content: {result.page_content}\n (Page Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])



SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers user query based on the available
context retrieved from a PDF file along with page_content and page number.

You should only ans the user based on the following context and navigate the 
user to open the right page number to know more 

context:
{context}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=[
        {
            "role": "user",
            "parts": [{"text": SYSTEM_PROMPT + "\n\nUser Query: " + user_query}]
        }
    ]
)
print(response.text)







