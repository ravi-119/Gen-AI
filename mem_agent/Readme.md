# 🧠 The Memory Layer in AI Agents

## Introduction

Modern AI agents are no longer simple prompt–response systems.  
To behave intelligently, agents must **remember**, **learn from past interactions**, and **use knowledge over time**.  
This is where the **Memory Layer** becomes critical.

This README explains:
- What memory means in AI agents
- Different memory architectures
- Short-term vs long-term memory
- Factual, episodic, and semantic memory
- How to use **Mem0** with Python
- How vector databases power AI agent memory

---

## What Is Memory in AI and Agents?

In AI agents, **memory** is the ability to:
- Store information
- Retrieve relevant past data
- Use it to make better decisions

Without memory:
- Agents forget previous conversations
- No personalization is possible
- Every interaction starts from scratch

With memory:
- Agents become **context-aware**
- Agents improve over time
- Agents feel more human-like

---

## Different Types of Memory Architectures in AI and Agents

AI memory can be broadly divided into:

1. **Short-Term Memory (STM)** – temporary context
2. **Long-Term Memory (LTM)** – persistent storage
3. **Factual Memory** – structured facts
4. **Episodic Memory** – past experiences
5. **Semantic Memory** – general knowledge

Each type serves a different purpose in agent workflows.

---

## Short-Term Memory – Handling Context Windows

### What is it?
Short-term memory is the **context window** of an LLM.

### Characteristics:
- Lives only during a single request/session
- Limited by token size
- Lost after the response is generated

### Example:
- Chat history in the last few messages
- Temporary variables during reasoning

### Limitation:
LLMs forget everything once the context window is exceeded.

---

## Long-Term Memory – Persistent Knowledge

### What is it?
Long-term memory stores information **outside the LLM**, allowing persistence across sessions.

### Characteristics:
- Stored in databases
- Can be retrieved anytime
- Scales beyond token limits

### Examples:
- User preferences
- Previous conversations
- Learned facts

This is essential for **real-world AI agents**.

---

## Factual Memory for AI Agents

### What is it?
Factual memory stores **explicit facts**.

### Examples:
- User name is Ravi
- Preferred language is English
- Company policy rules

### Use cases:
- Accurate responses

Factual memory is usually structured and reliable.

---
```bash
pip install mem0
```

---

## Mem0 Configuration with Python for Agents

### Basic Setup

```python
from mem0 import Memory

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    },
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "agent_memory"
        }
    }
}

- Stores structured and unstructured memory
```

### Storing Memory
```python
memory.add(
    "User prefers cloud and DevOps topics",
    user_id="ravi"
)
```

### Retrieving Memory
```python
results = memory.search(
    "What topics does the user like?",
    user_id="ravi"
)

print(results)
```
- Handles embeddings automatically
- Works with LLM-based agents

