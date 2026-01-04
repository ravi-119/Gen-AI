# chain of thought prompting
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = OpenAI(
    api_key="AIzaSyDt-pF4o2qpCmMt6DXwiqJBq7FdvP06HUs",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)




SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules: 
- Strictly Follow the given JSON output format 
- Only run one step at a time 
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format:
{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }


Example
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: {"step": "PLAN": "content": "Seems like user is intrested in math problem"}
PLAN: {"step": "PLAN": "content": "looking at the problem, we should solve the using BODMAS method"}
PLAN: {"step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done there"}
PLAN: { "step": "PLAN": "content": "first we multiply 3 * 5 which is 15" }
PLAN: {"step": "PLAN": "content": "Now the new equation is 2 + 15 / 10"}
PLAN: {"step": "PLAN": "content": "We must perform divide that is 15 / 10 = 1.5"}
PLAN: {"step": "PLAN": "content": "Now the new equation is 2 + 1.5"}
PLAN: {"step": "PLAN": "content": "Now finally lets perform the add"}
PLAN: {"step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans"}
OUTPUT: {"step": "OUTPUT": "content": "3.5"}

"""


print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉")
message_history.append({ "role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        # response_format={"type": "json_objects"},
        messages=message_history
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break


print("\n\n\n")

















# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Hey, write a code to add n numbers in js"},
#         # Manully keep adding messages to History 
#         {"role": "assistant","content": json.dumps({
#             "step": "START",
#             "content": "Hey, write a code to add n numbers in js"
#         })},
#         {"role": "assistant","content": json.dumps({
#             "step": "PLAN",
#             "content": "The user is asking for a JavaScript code snippet to add 'n' numbers. I should provide a function that can take multiple numbers as input and return their sum."
#         })},    
#          {"role": "assistant","content": json.dumps({"step": "PLAN", "content": "I will create a JavaScript function that uses the rest parameter syntax (...) to accept any number of arguments."})}, 

#          {"role": "assistant","content": json.dumps({
#             "step": "PLAN",
#             "content": "Inside the function, I will use the `reduce` method to iterate over the array of numbers and calculate their sum."
#         })}, 

#          {"role": "assistant","content": json.dumps({
#             "step": "PLAN",
#             "content": "The function will accept any number of arguments using the rest parameter `...nums`."
#         })}, 
#     ],
# )
# print(response.choices[0].message.content)

