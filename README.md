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

The system is built as a directed graph of specialized AI agents with parallel execution:

```mermaid
graph TD
    A[Job Analyzer] --> B[Profile Builder]
    A --> C[Resume Strategist]
    B --> D[Content Refinement]
    C --> D
    D --> E[Interview Prep]
    E --> F[END]
```

**Agents:**
- **Job Analyzer**: Extracts key skills and requirements from job postings
- **Profile Builder**: Builds professional profiles using GitHub data and job analysis
- **Resume Strategist**: Creates tailored resume drafts based on job requirements
- **Content Refinement**: Improves resume clarity, structure, and professionalism
- **Interview Prep**: Generates interview questions and preparation tips

Each agent operates on a shared Pydantic state object and contributes to the final output.

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
- Qwen2.5:7b model
- Pydantic (structured state)
- Requests (API calls)
- Tavily (web search & content extraction)

---

# 📦 Installation

## Prerequisites

- Python 3.11+
- Ollama installed and running
- Qwen2.5:7b model downloaded
- Tavily API key (optional, for web search)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/damian-r-s/multi-agent-career-assistant.git
   cd multi-agent-career-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # for development
   ```

3. **Install Ollama and model:**
   ```bash
   # Install Ollama (if not already)
   curl -fsSL https://ollama.ai/install.sh | sh

   # Pull the model
   ollama pull qwen2.5:7b
   ```

4. **Set up API keys (optional):**
   ```bash
   # For web search functionality
   export TAVILY_API_KEY="your-tavily-api-key"
   ```

5. **Verify setup:**
   ```bash
   python main.py
   ```

---

# 🚀 Usage

## Basic Usage

```python
from input_handler import prepare_initial_state
import graph

# Prepare input
job_posting = "Senior Python Engineer with ML experience..."
initial_state = prepare_initial_state(job_posting)

# Run the system
result = graph.agent.invoke(initial_state)

print("Resume:", result['refined_output'])
print("Interview Prep:", result['interview_prep'])
```

## With Job Posting URL

```python
initial_state = prepare_initial_state(
    job_url="https://company.com/job-posting-url"
)
```

## With GitHub Profile

```python
initial_state = prepare_initial_state(
    job_posting="...",
    github_username="your-github-username"
)
```

## With Resume File

```python
initial_state = prepare_initial_state(
    job_posting="...",
    resume_path="/path/to/resume.txt"
)
```

## Command Line

```bash
python main.py
```

---

# 🧪 Development & Testing

## Running Tests

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest test/
```

## Adding New Agents

1. Create a new file in `agents/` directory
2. Implement the agent function that takes `state` and returns a dict
3. Add the agent to `graph.py`:
   - Import the function
   - Add node: `graph.add_node("agent_name", agent_function)`
   - Add edges: `graph.add_edge("previous_node", "agent_name")`

## Code Quality

- Use Pydantic for state validation
- Follow Python type hints
- Keep agents modular and focused on single responsibilities

---

# 📁 Project Structure

```
multi-agent-career-assistant/
├── agents/                    # Individual agent implementations
│   ├── content_refinement.py
│   ├── interview_prep.py
│   ├── job_analyzer.py
│   ├── profile_builder.py
│   └── resume_strategist.py
├── tools/                     # Utility tools
│   ├── file_reader.py
│   ├── github_api.py
│   └── job_tavil_client.py
├── test/                      # Tests and test data
│   ├── example-resume.txt
│   └── test_tools.py
├── graph.py                   # Main graph definition
├── input_handler.py           # Input processing
├── llm.py                     # LLM configuration
├── main.py                    # Entry point
├── state.py                   # Pydantic state model
├── requirements.txt           # Python dependencies
├── requirements-dev.txt       # Development dependencies
├── LICENSE
└── README.md
```

---

# 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

# 📄 License

MIT License - see LICENSE file for details

---

# 🙏 Acknowledgments

- LangGraph for the agent orchestration framework
- Ollama for local LLM support
- Qwen team for the excellent model

---