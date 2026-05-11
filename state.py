from typing import TypedDict, Optional

class AgentState(TypedDict):
    job_posting: str
    analysis: Optional[str]
    resume_draft: Optional[str]
    refined_output: Optional[str]