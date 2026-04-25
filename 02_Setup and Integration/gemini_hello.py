from google import genai


client = genai.Client(
    api_key="AIzaSyA6yEg6EHeNDkLyDVjE2BH77xmtdwEzjW8"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Explain how AI works in a few words"
)
print(response.text)


