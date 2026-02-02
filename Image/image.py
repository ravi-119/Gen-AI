from google import genai
from google.genai import types

import requests

image_path = "https://martech.org/wp-content/uploads/2014/09/content-marketing-ss-1920.jpg"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client(
    api_key=""
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["Generate a caption for this image in about 50 words", image],
)

print(response.text)

