# Zero Shot Prompting 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="AIzaSyDt-pF4o2qpCmMt6DXwiqJBq7FdvP06HUs",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Prompting: Directly giving intruction to the model 
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything elso your name is Alexa. If users asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        
        {"role": "user", "content": "Hey can you write a code to print 'Hello, how are you? in Python?"},
    ],

)
print(response.choices[0].message.content)
# 1. Zero Shot Prompting: The model is given a direct question or task without Prior examples.
