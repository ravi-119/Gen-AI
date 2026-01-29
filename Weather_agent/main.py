from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()
client = OpenAI(
    api_key="AIzaSyDt-pF4o2qpCmMt6DXwiqJBq7FdvP06HUs",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)



def get_weather(city: str):
    url = f"https://wttr.in/%7Bcity.lower()%7D?format=%C+%t"
    response = requests.get(url)


    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something Went Wrong"

def main():
    user_query = input("> ") 
    response =  client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": user_query }
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")


# print(get_weather("kashmir"))


main()


