from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load env variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model with "agent-like" system instructions
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You're an agent which greets the user and helps them "
        "using emojis and in a funny way."
    )
)

# User input
user_input = "Hey There, My Name is Ravi"

# Generate response
response = model.generate_content(user_input)

print(response.text)
