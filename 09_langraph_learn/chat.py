from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    # model_provider="google_genai",
)

class State(TypedDict):
    messages: Annotated[list, add_messages]  


def chatbot(state: State):
    # print("\n\nInside chatbot node", state)
    response = llm.invoke(state.get("messages"))
    return { "messages": [response]}


def samplenode(state: State):
    print("\n\nInside samplenode node", state)
    return { "messages": ["Sample Message Appended"]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, My name is Ravi Yadav"]}))
print("\n\nupdated_state", updated_state)

# (START)  -> chatbot  -> samplenode -> (END)
# state = {messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey There"]) -> ["Hi, this is a message from ChatBot Node"]
# state = {"messages": ["Hey there", "Hi, this is a message from ChatBot Node"]}

