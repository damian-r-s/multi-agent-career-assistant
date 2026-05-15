from pydantic import BaseModel, Field
from typing import Optional

class AgentState(BaseModel):
    job_posting: Optional[str] = Field(default=None, description="The job posting text to analyze")
    github_profile: Optional[str] = Field(default=None, description="GitHub profile URL or data")
    resume_file: Optional[str] = Field(default=None, description="Path to resume file")    
    provider: Optional[str] = Field(default=None, description="LLM provider (e.g., 'ollama' or 'openai')")
    api_key: Optional[str] = Field(default=None, description="API key for online LLM providers")
    ollama_model: Optional[str] = Field(default=None, description="Model name for local Ollama (e.g., 'llama2', 'qwen2.5:7b')")
    analysis: Optional[str] = Field(default=None, description="Job analysis output")
    profile_data: Optional[str] = Field(default=None, description="Profile building output")
    resume_draft: Optional[str] = Field(default=None, description="Resume draft output")
    refined_output: Optional[str] = Field(default=None, description="Refined resume output")
    interview_prep: Optional[str] = Field(default=None, description="Interview preparation output")
