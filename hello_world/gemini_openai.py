from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="AIzaSyDt-pF4o2qpCmMt6DXwiqJBq7FdvP06HUs",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in Maths and only and only answer Maths related questions. If the question is not related to Maths, politely refuse to answer."},
        
        {"role": "user", "content": "Hey can you code a python program that can print hello world?"}
    ],

)
print(response.choices[0].message.content)

