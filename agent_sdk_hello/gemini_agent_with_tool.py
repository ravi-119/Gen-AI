from dotenv import load_dotenv
import os
import requests
import google.generativeai as genai

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ---- TOOL FUNCTION ----
def get_weather(city: str):
    """Fetch weather for a city"""
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"

# ---- FUNCTION SCHEMA FOR GEMINI ----
weather_tool = {
    "name": "get_weather",
    "description": "Fetch the current weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "Name of the city"
            }
        },
        "required": ["city"]
    }
}

# ---- MODEL (AGENT BEHAVIOR) ----
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You're an agent which greets the user and helps them "
        "using emojis and in a funny way. "
        "If you need external info, ask for tools."
    ),
    tools=[{"function_declarations": [weather_tool]}]
)

# ---- USER QUERY ----
user_input = "What is on Piyushgarg.dev website?"

response = model.generate_content(user_input)

# ---- HANDLE TOOL CALLS ----
if response.candidates[0].content.parts[0].function_call:
    fc = response.candidates[0].content.parts[0].function_call
    args = fc.args

    if fc.name == "get_weather":
        tool_result = get_weather(**args)

        # Send tool result back to Gemini
        response = model.generate_content(
            [
                user_input,
                {
                    "role": "tool",
                    "name": fc.name,
                    "content": tool_result
                }
            ]
        )

print(response.text)
