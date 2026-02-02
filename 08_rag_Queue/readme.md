# RAG with Async Queues & Distributed Workers

This document provides a complete guide to building a **Retrieval-Augmented Generation (RAG)** system using **asynchronous queues** and **distributed workers**. It covers architecture, setup, coding patterns, and deployment best practices.

---

## Table of Contents

1. [Introduction](#introduction)  
2. [Architecture Overview](#architecture-overview)  
3. [Key Components](#key-components)  
4. [Setting Up the Environment](#setting-up-the-environment)  
5. [Queue & Worker Implementation](#queue--worker-implementation)  
6. [Integrating RAG](#integrating-rag)  
7. [Async Workflow](#async-workflow)  
8. [Distributed Worker Setup](#distributed-worker-setup)  
9. [Error Handling & Monitoring](#error-handling--monitoring)  
10. [Deployment & Scaling](#deployment--scaling)  
11. [Example Code Snippets](#example-code-snippets)  
12. [References](#references)  

---

## Introduction

**RAG (Retrieval-Augmented Generation)** combines a **retrieval system** (knowledge base, vector DB) with a **generative model** (LLM). It allows large language models to answer queries using relevant context from documents.  

**Why Async Queues & Distributed Workers?**

- Handles high concurrency efficiently.  
- Offloads heavy processing from API endpoints.  
- Enables horizontal scaling with multiple workers.

---

## Architecture Overview

       ┌──────────────┐
       │   User/API   │
       └─────┬────────┘
             │ POST /chat
             ▼
       ┌──────────────┐
       │   Queue      │  (Redis / RabbitMQ)
       └─────┬────────┘
             │ Job Enqueue
             ▼
       ┌──────────────┐
       │  Worker(s)   │  (Distributed)
       └─────┬────────┘
             │ Fetch Docs from DB / Vector Store
             ▼
       ┌──────────────┐
       │  RAG Model   │  (LLM + Retriever)
       └─────┬────────┘
             │ Return Result
             ▼
       ┌──────────────┐
       │   API/DB     │
       └──────────────┘

---

## Key Components

1. **API Layer**  
   - Accepts user queries  
   - Pushes jobs to the queue  

2. **Queue System**  
   - Redis Queue (RQ) / Celery / RabbitMQ  
   - Handles async jobs  

3. **Workers**  
   - Consume queue jobs  
   - Fetch relevant documents from vector store  
   - Run LLM generation  

4. **Retriever**  
   - Vector DB (e.g., FAISS, Pinecone, Weaviate)  
   - Finds top-k relevant docs  

5. **Generator**  
   - LLM (OpenAI, HuggingFace, or local LLM)  
   - Produces final answers using retrieved context  

---

## Setting Up the Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn redis rq python-dotenv transformers faiss-cpu
REDIS_URL=redis://localhost:6379
VECTOR_DB_PATH=./vector_store
LLM_MODEL=your-llm-model





# RQ Worker on Windows vs Linux

This document explains a common issue with running **RQ workers** on Windows and how to fix it.

---

## Problem

When running RQ workers on Windows, you might see the following error:


### Why this happens

RQ uses **`os.fork()`** to run jobs in child processes.  

- **Linux/macOS:** `fork()` is supported ✅  
- **Windows:** `fork()` is **not available** ❌

**Flow of failure on Windows:**

1. Worker starts ✅  
2. Job arrives ✅  
3. RQ tries to fork ❌  
4. Worker crashes → jobs marked `AbandonedJobError` → `0 workers` shown in `rq info`

---

## Common Misconception

Setting the environment variable:

OBJC_DISABLE_INITIALIZE_FORK_SAFETY



- Only affects **macOS**.  
- Does **not** solve the Windows issue.

---

## Solutions

### 1. Best Fix: Use WSL (Windows Subsystem for Linux) ✅

1. Install WSL:

```bash
wsl --install



Open Ubuntu terminal, install Python & Redis:

sudo apt update
sudo apt install python3 python3-pip redis-server
pip install rq redis


Start Redis:

sudo service redis-server start


Run the worker:

rq worker --with-scheduler


Fork works

No crashes

Jobs run properly

2. Alternative (Without WSL): Use SimpleWorker 🟡

RQ 2.x supports a Windows-compatible worker:

rq worker --with-scheduler --worker-class rq.worker.SimpleWorker


No fork()

Slower performance

Works on Windows for development/testing

3. Another Option: rq-win 🔹
pip install rq-win
rqworker


Works on Windows

Less recommended than SimpleWorker or WSL

Why this Fixes Everything
Problem	Cause
Worker crashes	fork() not available
AbandonedJobError	Worker dies mid job
0 workers in rq info	Process exited
Recommendations

For AI/ML or heavy backend jobs, use WSL or Linux

Avoid running resource-heavy jobs on native Windows RQ workers

Use SimpleWorker for quick development/testing on Windows

Temporary Fix on Windows
rq worker --with-scheduler --worker-class rq.worker.SimpleWorker


Your jobs should start executing immediately.

Note: Once running in WSL/Linux, the fork-based worker is faster and stable for production workloads.

