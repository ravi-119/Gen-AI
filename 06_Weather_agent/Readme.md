# 🤖 Agentic AI Fundamentals & CLI Coding Agent

This project and notes summarize the **core concepts of Agentic AI**, what **AI Agents** really are, and how to **enforce structured outputs using Pydantic**, along with an implementation of a **CLI-based coding agent**.

---

## 🧠 What is Agentic AI?

**Agentic AI** refers to AI systems that don’t just respond — they **act with autonomy** to achieve goals.

Instead of:
> Prompt → Response

We get:
> Goal → Reasoning → Tool Use → Actions → Observation → Iteration → Result

Agentic systems behave more like **decision-makers** than simple text generators.

### 🔑 Key Properties of Agentic AI

| Feature | Description |
|---------|-------------|
| 🎯 Goal-driven | Works toward a defined objective |
| 🧠 Reasoning | Breaks problems into steps |
| 🔁 Iterative | Learns from intermediate outputs |
| 🛠 Tool usage | Uses APIs, code, search, files, etc. |
| 👀 Observability | Tracks environment + results |
| 🧩 Planning | Decides *what to do next* |

---

## 🤖 What Exactly Are AI Agents?

An **AI Agent** is a system powered by an LLM that can:

> **Perceive → Think → Decide → Act**

### 🧱 Core Components of an AI Agent

1. **LLM (Brain)**  
   Handles reasoning, planning, and decision-making.

2. **Tools (Hands)**  
   Functions or APIs the agent can call:
   - Code execution
   - File operations
   - Web search
   - Database queries

3. **Memory (Context)**  
   Stores conversation history or task state.

4. **Planner / Controller (Loop Logic)**  
   Sends prompts, parses outputs, and decides next action.  

---

## 🧩 Structured Outputs with Pydantic

- **LLMs often return unstructured text**, which is hard for programs to handle.
- **Using Pydantic, we can enforce structured, validated outputs.**

### ❌ Without Structure
```
"I think you should use the file tool and then generate code."
```

### ✅ With Pydantic
```python
from pydantic import BaseModel
from typing import Literal, Optional

class AgentAction(BaseModel):
    tool: Literal["code", "search", "file", "none"]
    input: str
    reasoning: Optional[str]
```

**LLM now outputs:**
```json
{
  "tool": "code",
  "input": "Write a Python function for factorial",
  "reasoning": "User wants code generation"
}
```

### 🚀 Benefits

| Benefit | Why It Matters |
|---------|---------------|
| 🧱 Reliability | No random format |
| 🛡 Validation | Wrong output = error caught |
| 🔧 Tool routing | Easy to decide which tool to call |
| 🤖 Real agents | Enables automation |

**Structured outputs make LLMs controllable systems, not just chatbots.**




### 🔄 Agent Loop (Simplified)

```text
User Goal
   ↓
LLM decides next action
   ↓
Tool is called
   ↓
Result is returned
   ↓
LLM observes result
   ↓
Repeat until goal achieved
```

---

## 💻 My Project: Weather Agent with Chain of Thought

A **Weather AI Agent** powered by Google Gemini that uses **Chain of Thought (CoT) prompting** to reason step-by-step before answering queries.

### 🎯 Purpose

- Takes user queries about weather
- Uses Chain of Thought to PLAN the approach
- Calls tools (weather API) when needed
- Returns structured, reasoned outputs

### ⚙️ Architecture

```
User Query (CLI Input)
   ↓
System Prompt (Chain of Thought Instructions)
   ↓
Gemini 2.5 Flash (LLM)
   ↓
Pydantic Structured Output (JSON)
   ↓
Tool Execution (get_weather)
   ↓
Observation & Iteration
   ↓
Final Output to User
```

### 🧠 Capabilities

- **Chain of Thought Reasoning**: Plans before acting
- **Tool Integration**: Calls weather API when needed
- **Structured Responses**: JSON output with step tracking
- **Iterative Loops**: START → PLAN → TOOL → OUTPUT

### 🛠 Tech Stack

- **Python** - Core language
- **Google Generative AI (Gemini)** - LLM backbone
- **Pydantic** - Structured output validation
- **Requests** - HTTP client for weather API
- **python-dotenv** - Environment variable management

### 🧭 How It Works

1. **START**: User provides a query
2. **PLAN**: LLM reasons about the approach (multiple PLAN steps)
3. **TOOL**: If needed, calls available tools (get_weather)
4. **OBSERVE**: Processes tool output
5. **OUTPUT**: Returns final answer to user

### 🛠 Installation

Install required packages:

```bash
pip install google-genai python-dotenv requests pydantic
```

### 🚀 Running the Agent

```bash
python agent.py
👉 What is the current weather of Delhi
```

### 📊 Example Output

```
🔥 START: Processing your weather query...
🧠 Seems like user is interested in getting weather of Delhi
🧠 Let's see if we have any available tools
🧠 Great, we have get_weather tool available
🔧 get_weather (Delhi) = The weather in Delhi is Partly cloudy 28°C
🧠 Great, I got the weather about Delhi
🤖 The current weather in Delhi is 28°C with partly cloudy conditions
```

---

## 🧭 Key Learnings

- How agents differ from normal LLM apps
- Why structure is critical in AI systems
- How Pydantic turns LLM output into real software inputs
- How tool-calling enables automation
- How to design reasoning loops

## 🚀 Future Improvements

- Add memory system for conversation history
- Add file system access for saving results
- Add code execution sandbox
- Multi-step planning capabilities
- Error recovery loop

---

## 🏁 Conclusion

**Agentic AI is the future of intelligent systems.**

By combining:
- **LLMs** (Reasoning)
- **Tools** (Action)
- **Pydantic** (Structure)
- **Agent Loops** (Control)

We move from **chatbots → autonomous problem solvers**.

Agent Loops (Control)

we move from chatbots → autonomous problem solvers.
