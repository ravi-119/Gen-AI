from dotenv import load_dotenv
from openai import OpenAI   
 
load_dotenv()


client = OpenAI() 


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user", 
            "content": [
                {"type": "text", "text": "Generate a caption for this image in about 50 words"},
                { "type": "image_url", "image_url": {"url": "https://www.freepik.com/free-photo/content-concept-laptop-screen_2755663.htm#fromView=keyword&page=1&position=1&uuid=09fae3e9-97df-4586-b653-532272af1326&query=Content"}}
            ]
        }
    ]
)
print("Response", response.choices[0].message.content)
