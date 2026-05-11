# 🧠 Multi-Agent Career Assistant

A production-style multi-agent AI system built with LangGraph and local LLMs (Ollama) that helps software engineers optimize their career path.

The system analyzes job postings, evaluates candidate profiles, and generates personalized outputs such as:
- Resume optimization
- Skill gap analysis
- Interview preparation
- Career recommendations

---

# 🚀 Key Features

- 🧩 Multi-agent architecture using LangGraph
- 🧠 Local LLM support (Ollama: Llama / Qwen / Mistral)
- 📄 Job posting analysis
- 👤 Candidate profile extraction (GitHub + resume)
- ✍️ Resume tailoring (ATS optimization)
- 🎯 Interview question generation
- 📊 Skill gap analysis
- 🔄 State-based workflow execution

---

# 🏗️ System Architecture

The system is built as a directed graph of specialized AI agents:

- Job Analyzer Agent
- Profile Analyzer Agent
- Resume Strategist Agent
- Interview Prep Agent

Each node operates on a shared state object and contributes to the final output.

---

# 🧠 Why LangGraph?

Unlike traditional agent frameworks, LangGraph provides:

- Explicit control over execution flow
- Stateful multi-step reasoning
- Deterministic orchestration
- Production-grade agent pipelines

---

# 🛠️ Tech Stack

- Python 3.11
- LangGraph
- LangChain
- Ollama (local LLM runtime)
- Qwen / Llama models
- Pydantic
- Rich (debugging & logs)

---