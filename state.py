from pydantic import BaseModel, Field
from typing import Optional

class AgentState(BaseModel):
    job_posting: str = Field(description="The job posting text to analyze")
    github_profile: Optional[str] = Field(default=None, description="GitHub profile URL or data")
    resume_file: Optional[str] = Field(default=None, description="Path to resume file")
    analysis: Optional[str] = Field(default=None, description="Job analysis output")
    profile_data: Optional[str] = Field(default=None, description="Profile building output")
    resume_draft: Optional[str] = Field(default=None, description="Resume draft output")
    refined_output: Optional[str] = Field(default=None, description="Refined resume output")
    interview_prep: Optional[str] = Field(default=None, description="Interview preparation output")