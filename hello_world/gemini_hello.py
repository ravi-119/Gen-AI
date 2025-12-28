from google import genai


client = genai.Client(
    api_key="AIzaSyDt-pF4o2qpCmMt6DXwiqJBq7FdvP06HUs"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Explain how AI works in a few words"
)
print(response.text)


