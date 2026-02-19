from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -----------------------------
# TRANSLATION FUNCTIONS (AGENTS)
# -----------------------------
def translate_to_spanish(text: str) -> str:
    return f"Spanish Translation: Hola, ¿cómo estás?"

def translate_to_french(text: str) -> str:
    return f"French Translation: Bonjour, comment ça va ?"

# -----------------------------
# FUNCTION SCHEMAS
# -----------------------------
tools = [
    {
        "name": "translate_to_spanish",
        "description": "Translate the user's message to Spanish",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string"}
            },
            "required": ["text"]
        }
    },
    {
        "name": "translate_to_french",
        "description": "Translate the user's message to French",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string"}
            },
            "required": ["text"]
        }
    }
]

# -----------------------------
# ORCHESTRATOR MODEL
# -----------------------------
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You are a translation orchestrator agent. "
        "Decide which translation tools to call. "
        "If the user asks for multiple translations, call all relevant tools."
    ),
    tools=[{"function_declarations": tools}]
)

# -----------------------------
# USER INPUT
# -----------------------------
user_input = "Say 'Hello, how are you?' in Spanish."

response = model.generate_content(user_input)

final_outputs = []

# -----------------------------
# TOOL EXECUTION LOOP
# -----------------------------
for part in response.candidates[0].content.parts:
    if hasattr(part, "function_call"):
        name = part.function_call.name
        args = part.function_call.args

        if name == "translate_to_spanish":
            final_outputs.append(translate_to_spanish(**args))

        elif name == "translate_to_french":
            final_outputs.append(translate_to_french(**args))

# -----------------------------
# FINAL OUTPUT
# -----------------------------
print("RAW TOOL OUTPUTS:")
print(final_outputs)

print("\nFINAL OUTPUT:")
print("\n".join(final_outputs))
