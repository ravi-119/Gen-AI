# Few Shot Prompting
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="AIzaSyDt-pF4o2qpCmMt6DXwiqJBq7FdvP06HUs",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# few Shot Prompting: Directly giving intruction to the model and few examples to the model 
SYSTEM_PROMPT = """You should only and only ans the coding related questions. Do not ans anything elso your name is Alexa. If users asks something other than coding, just say sorry.


Rule: 
-Strictly follow the output in JSON format.

Output Format:
{{
    "code": "string or null,
    "isCodingQuestion": "boolean"
}}

Examples:
Q: Can you explain the a + b whole squre?
A: {{"code": null, "isCodingQuestion": false}}

Q: Hey Write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
            return a + b", "isCodingQuestion": true }}


""" 

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        
        {"role": "user", "content": "Hey can you write a code to print 'Hello, how are you? in Python?"},

        #  {"role": "user", "content": "Hey can you explain a + b whole square"},
    ],

)
print(response.choices[0].message.content)
# 1. few short Prompting: The model is given a direct question or task along with prior examples to guide its response.




