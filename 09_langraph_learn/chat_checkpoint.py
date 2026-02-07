from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.mongodb import MongoDBSaver 

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

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


graph = graph_builder.compile()



def compile_graph_with_checkpoint(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)


DB_URI = "mongodb://localhost:27017/"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpoint(checkpointer=checkpointer)

    config = {
            "configurable": {
                "thread_id": "Ravi"
            }
        }

    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["What am I learning"]}),
        config,
        stream_mode="values"
        ):
            chunk["messages"][-1].pretty_print()



# (START)  -> chatbot -> (END)
# state = {messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey There"]) -> ["Hi, this is a message from ChatBot Node"]
# state = {"messages": ["Hey there", "Hi, this is a message from ChatBot Node"]}

# Checkpointer (Ravi) = Hey My name is Ravi Yadav




