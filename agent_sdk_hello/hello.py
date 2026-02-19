from dotenv import load_dotenv 
from agents import Agent, Runner
import os
load_dotenv()


# Define a agent 
hello_agent = Agent (
    name="Hello World Agent",
    instructions="You're an agent which greets the user and helps them ans using emojis and in funny way."
)

result = Runner.run_sync(hello_agent, "Hey There, My Nmae is Ravi")
print(result)
