from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import tempfile
from pathlib import Path

from src.state import AgentState
from src.input_handler import prepare_initial_state
from src import graph
from src.llm import llm

app = FastAPI(title="Career Assistant API")

# Mount static files
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def root():
    """Serve the main HTML page"""
    return FileResponse("static/index.html")

@app.post("/api/analyze")
async def analyze(job_url: str = Form(...),  github_username: str = Form(default=None), resume_file: UploadFile = File(default=None), provider: str = Form(default=None), api_key: str = Form(default=None), ollama_model: str = Form(default=None)):
    """
    Analyze job posting and generate career recommendations.
    
    Args:
        job_url: URL to the job posting
        github_username: GitHub username (optional)
        resume_file: Resume file upload (optional)
    
    Returns:
        Analysis results including refined resume and interview prep
    """
    try:
        # Save uploaded resume to temp file if provided
        resume_path = None
        if resume_file and resume_file.filename:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
                content = await resume_file.read()
                tmp.write(content.decode('utf-8'))
                resume_path = tmp.name
        
        # Prepare initial state (include optional provider/api_key)
        print(f"Processing: job_url={job_url}, github={github_username}, resume={resume_path}, provider={provider}")
        initial_state = prepare_initial_state(
            job_url=job_url,
            github_username=github_username,
            resume_path=resume_path,
            provider=provider,
            api_key=api_key,
            ollama_model=ollama_model
        )
        # If a provider/api_key/ollama_model is supplied, set the LLM override for this request
        if provider or api_key or ollama_model:
            llm.set_override(provider, api_key, ollama_model)
        
        # Run the multi-agent graph
        print("Running analysis graph...")
        final_state = graph.agent.invoke(initial_state)
        
        # Clean up temp file
        if resume_path and os.path.exists(resume_path):
            os.unlink(resume_path)
        
        return {
            "status": "success",
            "data": {
                "analysis": final_state.get('analysis', ''),
                "profile_data": final_state.get('profile_data', ''),
                "resume_draft": final_state.get('resume_draft', ''),
                "refined_output": final_state.get('refined_output', ''),
                "interview_prep": final_state.get('interview_prep', '')
            }
        }
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        llm.clear_override()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
