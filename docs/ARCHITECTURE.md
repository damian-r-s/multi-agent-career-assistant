# 🏗️ Architecture Documentation

## System Overview

This document describes the architecture of the Multi-Agent Career Assistant system.

The system is deployed publicly at:

👉 **https://multi-agent-career-assistant.onrender.com/**

Production environment:
- Render Cloud (Docker)
- FastAPI backend
- Static frontend served from the same container
- External/local Ollama LLM

## 🧩 Component Architecture

The system is built as a directed acyclic graph (DAG) of specialized AI agents that process information through multiple stages:

```
┌─────────────────────────────────────────────────────────────┐
│                        Input Handler                         │
│  (Job URL, GitHub Username, Resume File)                    │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
      Tavily API    GitHub API      File Reader
         │               │               │
         └───────────────┼───────────────┘
                         │
                ┌────────▼────────┐
                │ AgentState      │
                │ (Pydantic Model)│
                └────────┬────────┘
                         │
         ┌───────────────┴───────────────┐
         │                               │
    ┌────▼─────────────┐    ┌──────────▼──────────┐
    │  Job Analyzer    │    │  Profile Builder    │
    │                  │    │                     │
    │ Extracts:        │    │ Builds:             │
    │ - Key skills     │    │ - Professional      │
    │ - Requirements   │    │   profile           │
    │ - Responsibilities    │ - From GitHub data  │
    └────┬─────────────┘    └──────────┬──────────┘
         │                              │
         └──────────┬───────────────────┘
                    │
         ┌──────────▼──────────────┐
         │  Resume Strategist      │
         │                         │
         │ Creates tailored        │
         │ resume draft            │
         └──────────┬──────────────┘
                    │
         ┌──────────▼──────────────┐
         │ Content Refinement      │
         │                         │
         │ Improves:               │
         │ - Clarity               │
         │ - Structure             │
         │ - Professionalism       │
         └──────────┬──────────────┘
                    │
         ┌──────────▼──────────────┐
         │  Interview Prep         │
         │                         │
         │ Generates:              │
         │ - Interview questions   │
         │ - Preparation tips      │
         └──────────┬──────────────┘
                    │
         ┌──────────▼──────────────┐
         │   Final Output          │
         │ (All results)           │
         └─────────────────────────┘
```

## 📂 Directory Structure

```
multi-agent-career-assistant/
│
├── src/                           # All source code
│   ├── __init__.py
│   ├── state.py                   # Pydantic state model (AgentState)
│   ├── llm.py                     # LLM configuration (Ollama ChatOllama)
│   ├── graph.py                   # LangGraph definition (DAG of agents)
│   ├── input_handler.py           # Input processing and state initialization
│   │
│   ├── agents/                    # Specialized agent implementations
│   │   ├── __init__.py
│   │   ├── job_analyzer.py        # Analyzes job postings
│   │   ├── profile_builder.py     # Builds professional profiles
│   │   ├── resume_strategist.py   # Creates tailored resume drafts
│   │   ├── content_refinement.py  # Polishes and optimizes content
│   │   └── interview_prep.py      # Generates interview prep materials
│   │
│   └── tools/                     # External service integrations
│       ├── __init__.py
│       ├── file_reader.py         # Reads local files
│       ├── github_api.py          # GitHub API client
│       └── job_tavil_client.py    # Tavily API for web extraction
│
├── static/                        # Frontend SPA files
│   ├── index.html                 # Single-page application
│   ├── style.css                  # CSS styling
│   └── script.js                  # Frontend JavaScript logic
│
├── test/                          # Test suite
│   ├── __init__.py
│   ├── test_tools.py              # Tool unit tests
│   └── example-resume.txt         # Test data
│
├── docs/                          # Documentation
│   ├── WEB_UI_GUIDE.md            # Web UI setup and usage
│   └── ARCHITECTURE.md            # This file
│
├── app.py                         # FastAPI web server
├── main.py                        # CLI entry point
├── requirements.txt               # Python dependencies
├── requirements-dev.txt           # Development dependencies
├── README.md                      # Project overview
├── LICENSE                        # License
└── .gitignore                    # Git ignore rules
```

## 🔄 Data Flow

### 1. Input Phase
```
User Input (URL, GitHub, Resume)
    ↓
input_handler.prepare_initial_state()
    ↓
Fetch job posting (Tavily)
Fetch GitHub profile (GitHub API)
Read resume file (File Reader)
    ↓
AgentState object created
```

### 2. Processing Phase
```
AgentState
    ↓
job_analyzer()
    ├─→ Extract key skills
    ├─→ Extract requirements
    └─→ Store in state.analysis
    ↓
[Parallel] Profile Builder & Resume Strategist
    ├─→ profile_builder() → state.profile_data
    └─→ resume_strategist() → state.resume_draft
    ↓
content_refinement()
    ├─→ Improve clarity
    ├─→ Improve structure
    └─→ Store in state.refined_output
    ↓
interview_prep()
    ├─→ Generate interview questions
    ├─→ Generate prep tips
    └─→ Store in state.interview_prep
    ↓
Final AgentState with all outputs
```

### 3. Output Phase
```
FastAPI returns JSON response
    ↓
Frontend displays in tabs
    ↓
User can:
    ├─→ Copy resume
    ├─→ Download all results
    └─→ Start new analysis
```

## 🧠 Agent Specifications

### Job Analyzer
- **Input**: Job posting text
- **Task**: Extract key skills, requirements, responsibilities
- **Output**: JSON/structured analysis
- **LLM Prompt**: "Extract key skills and requirements from this job: ..."

### Profile Builder
- **Input**: Job analysis + GitHub profile data
- **Task**: Build professional profile matching job requirements
- **Output**: Professional profile summary
- **LLM Prompt**: "Build a professional profile based on job analysis and GitHub data..."

### Resume Strategist
- **Input**: Job analysis + Profile data
- **Task**: Create tailored resume draft
- **Output**: Resume text formatted for the role
- **LLM Prompt**: "Based on job analysis, create a tailored resume draft..."

### Content Refinement
- **Input**: Resume draft
- **Task**: Improve clarity, structure, professionalism
- **Rules**: Don't add new facts, improve readability, maintain professionalism
- **Output**: Polished resume
- **LLM Prompt**: Includes specific rules to prevent hallucination

### Interview Prep
- **Input**: Job posting + Analysis + Refined resume
- **Task**: Generate interview questions and preparation tips
- **Output**: Interview questions and tips specific to the role
- **LLM Prompt**: "Prepare interview questions and tips based on job analysis..."

## 🔗 Technology Stack

### Backend
- **FastAPI**: Web framework for API endpoints
- **LangChain/LangGraph**: Multi-agent orchestration and state management
- **Ollama**: Local LLM runtime (no API keys needed)
- **Pydantic**: Data validation and state definition

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with gradient backgrounds and animations
- **JavaScript (Vanilla)**: UI interactions, API calls

### External Services
- **GitHub API**: Fetch user profile and repositories
- **Tavily API**: Extract content from job posting URLs
- **Ollama LLM**: Local language model inference

### Development
- **pytest**: Unit testing framework
- **uvicorn**: ASGI server
- **python-multipart**: File upload handling

## 🔌 API Design

### REST Endpoints

#### POST /api/analyze
Analyzes job and generates career recommendations.

**Request:**
```json
{
  "job_url": "https://example.com/job",
  "github_username": "optional-username",
  "resume_file": "optional-file.txt"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "analysis": "...",
    "profile_data": "...",
    "resume_draft": "...",
    "refined_output": "...",
    "interview_prep": "..."
  }
}
```

#### GET /health
System health check.

**Response:**
```json
{"status": "ok"}
```

## 🔐 State Management

The entire system uses a single **AgentState** (Pydantic BaseModel):

```python
class AgentState(BaseModel):
    job_posting: str              # Input: job text
    github_profile: Optional[str] # Input: GitHub data
    resume_file: Optional[str]    # Input: resume text
    analysis: Optional[str]       # Output: job analysis
    profile_data: Optional[str]   # Output: profile summary
    resume_draft: Optional[str]   # Output: initial resume
    refined_output: Optional[str] # Output: polished resume
    interview_prep: Optional[str] # Output: interview materials
```

**Advantages:**
- Type-safe: Pydantic validates all data
- Immutable flow: Each agent only adds new fields
- Traceable: All transformations visible in final state
- Testable: Each agent can be tested independently

## 🎯 Execution Flow (LangGraph)

LangGraph manages the execution order:

1. **Job Analyzer** starts first (entry point)
2. **Profile Builder** and **Resume Strategist** run in parallel
3. **Content Refinement** waits for both to complete
4. **Interview Prep** runs last
5. All results merged into final state

This DAG structure ensures:
- Maximum parallelization (4 → 2 → 1 pipeline)
- Deterministic ordering
- No circular dependencies
- Easy to add/remove agents

## 🚀 Deployment Architecture

### Local Development
```
Browser → FastAPI (local:8000) → LangGraph → Ollama (local:11434)
                  ↓ (static files)
                static/
```

### Docker Deployment
```
Browser → FastAPI Container
             ↓
          LangGraph
             ↓
          Ollama Container
```

## 📊 Performance Considerations

1. **Parallel Execution**: Job Analyzer fan-out to 2 agents saves ~33% time
2. **Local LLM**: Ollama runs locally, no API latency
3. **File Uploads**: Temp files cleaned up automatically
4. **Caching**: GitHub/web requests could be cached between analyses

## 🔄 Error Handling

- **File not found**: Returns None, skipped in pipeline
- **API failures**: Error message passed to LLM
- **LLM errors**: Caught and returned to user
- **Upload failures**: 413 error with helpful message

## 📈 Future Extensibility

### Adding New Agents
1. Create file in `src/agents/`
2. Implement function with signature: `def agent_name(state) -> dict`
3. Add to `src/graph.py`: `graph.add_node()` and `graph.add_edge()`
4. New fields automatically added to AgentState

### Adding New Tools
1. Create file in `src/tools/`
2. Implement service function
3. Import and use in input_handler or agents

### Adding New Outputs
1. Add field to AgentState
2. Populate in agent functions
3. Frontend automatically displays in new tab

## 🧪 Testing Strategy

- **Unit Tests**: Test each tool independently (mocked API calls)
- **Integration Tests**: Test agent graph execution
- **End-to-End Tests**: Full pipeline with real data

See `test/test_tools.py` for examples.
