# Persona Based Thought prompting 
from openai import OpenAI
from dotenv import load_dotenv


import os
import json

load_dotenv()
client = OpenAI(
    api_key="AIzaSyDt-pF4o2qpCmMt6DXwiqJBq7FdvP06HUs",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


System_PROMPT = """      
    You are an AI Persona Assistant named Ravi Kumar Yadav.
    You are acting on behalf of Ravi Kumar Yadav who is 22 years old Tech enthusiastic and Principle engineer. Your main tech stack is JS and python and you are learning GenAI these days.
    Examples:
    Q. Hey 
    A: Hey, Whats up!

    (100 - 150 examples)

"""
   



response = client.chat.completions.create(
        model="gemini-2.5-flash",
        # response_format={"type": "json_objects"},
        messages=[
            {"role": "system", "content": System_PROMPT},
            {"role": "user", "content": "who are you"}
        ]
    )


print("Response:", response.choices[0].message.content)

