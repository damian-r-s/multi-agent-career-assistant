# Web UI Setup Guide

This guide explains how to run the web-based Career Assistant with the FastAPI backend and HTML/JavaScript frontend.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Ollama (if not already running)

```bash
ollama serve
```

In another terminal, ensure your model is ready:
```bash
ollama list  # Check if qwen2.5:7b is available
ollama pull qwen2.5:7b  # If not available
```

### 3. Set Environment Variables (optional)

```bash
export TAVILY_API_KEY="your-api-key-here"
```

### 4. Start the Web Server

```bash
python app.py
```

Or alternatively:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### 5. Access the Application

Open your browser and navigate to:
```
http://localhost:8000
```

---

## 🎨 Web UI Features

### Input Form
- **Job Posting URL** (required): Paste the URL of the job posting you want to analyze
- **GitHub Username** (optional): Your GitHub profile will be analyzed for skills, projects, and contributions
- **Resume File** (optional): Upload your resume (TXT, PDF, DOC, DOCX supported)

### Results Display
The results are organized in tabs:

1. **Job Analysis** - Key skills, requirements, and responsibilities extracted from the job posting
2. **Profile Data** - Your GitHub profile information and project analysis
3. **Resume Draft** - Initial resume tailored to the job requirements
4. **Refined Resume** - Final polished resume with improved formatting and ATS optimization
5. **Interview Prep** - Common interview questions and preparation tips specific to the role

### Actions
- **Copy Resume** - Copy the refined resume to your clipboard
- **Download All** - Download all results as a single text file
- **New Analysis** - Clear results and start a new analysis

---

## 📁 Project Structure

```
project-root/
├── app.py                          # FastAPI backend server
├── static/                         # Frontend files (served by FastAPI)
│   ├── index.html                 # Main HTML page
│   ├── style.css                  # Styling
│   └── script.js                  # Frontend JavaScript logic
├── requirements.txt               # Python dependencies
├── graph.py                       # Multi-agent graph definition
├── state.py                       # State management
├── input_handler.py               # Input processing
└── agents/                        # Individual agents
    ├── job_analyzer.py
    ├── profile_builder.py
    ├── resume_strategist.py
    ├── content_refinement.py
    └── interview_prep.py
```

---

## 🔧 API Endpoints

### GET /
Returns the main HTML page (single-page application).

### POST /api/analyze
Analyzes a job posting and generates recommendations.

**Request:**
```
multipart/form-data:
- job_url (string, required): URL of the job posting
- github_username (string, optional): GitHub username
- resume_file (file, optional): Resume file upload
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

### GET /health
Health check endpoint.

```json
{"status": "ok"}
```

---

## 💡 Usage Examples

### Via Web UI (Recommended)
1. Open http://localhost:8000
2. Paste a job URL (e.g., from LinkedIn, Google Jobs, etc.)
3. Optionally add your GitHub username and/or resume file
4. Click "Analyze Position"
5. Review results in the tabs
6. Copy the refined resume or download all results

### Programmatically with cURL
```bash
curl -X POST http://localhost:8000/api/analyze \
  -F "job_url=https://example.com/job-posting" \
  -F "github_username=your-username" \
  -F "resume_file=@path/to/resume.txt"
```

### Python Client
```python
import requests

files = {
    'resume_file': open('resume.txt', 'rb')
}

data = {
    'job_url': 'https://example.com/job-posting',
    'github_username': 'your-username'
}

response = requests.post('http://localhost:8000/api/analyze', files=files, data=data)
print(response.json())
```

---

## ⚙️ Configuration

### Change Port
```bash
uvicorn app:app --port 8080 --host 0.0.0.0
```

### Enable Auto-Reload (Development)
```bash
uvicorn app:app --reload
```

### Change LLM Model
Edit `llm.py` to use a different Ollama model:
```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="mistral",  # Change from qwen2.5:7b to another model
    temperature=0.7,
    base_url="http://localhost:11434"
)
```

---

## 🐛 Troubleshooting

### Issue: "Cannot connect to Ollama"
**Solution:** Make sure Ollama is running:
```bash
ollama serve
```

### Issue: "Model not found"
**Solution:** Pull the model:
```bash
ollama pull qwen2.5:7b
```

### Issue: Upload fails with 413 error
**Solution:** FastAPI has a default max file size. Update `app.py`:
```python
app = FastAPI(max_request_size=10*1024*1024)  # 10MB
```

### Issue: Results are empty
**Solution:** Check the terminal logs for errors. Ensure:
1. Ollama is running
2. TAVILY_API_KEY is set (if using job URL extraction)
3. GitHub API is accessible (if using GitHub username)

---

## 📊 Performance Tips

- **First run**: The first analysis may take longer as the LLM warms up
- **Parallel processing**: Job Analyzer, Profile Builder, and Resume Strategist run in parallel
- **Caching**: Consider adding caching for GitHub and web requests
- **Local LLM**: Using a local Ollama model means no network latency for inference

---

## 🔐 Security Notes

1. **API Keys**: Never commit `.env` files with API keys
2. **File Uploads**: Currently no file type validation - add if needed
3. **Rate Limiting**: Consider adding rate limiting for production
4. **CORS**: Configure CORS if deploying with a separate frontend

---

## 📦 Deployment

### Docker Deployment
```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose (with Ollama)
```yaml
version: '3'
services:
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - ollama
    environment:
      - OLLAMA_HOST=http://ollama:11434

volumes:
  ollama_data:
```

---

## 📝 Next Steps

1. **Add Authentication**: Implement user login/registration
2. **Database**: Store analysis history for users
3. **Export Formats**: Add PDF, DOCX export options
4. **Real-time Updates**: Use WebSockets for live processing updates
5. **Advanced Filtering**: Allow users to filter and customize agent behavior
