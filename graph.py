from langgraph.graph import StateGraph, END
from llm import llm
from state import AgentState

def job_analyzer(state: AgentState):
    print("🧠 Job Analyzer")
    
    prompt = f"Extract key skills and requirements from this job: {state['job_posting']}"
    response = llm.invoke(prompt)

    return {"analysis": response.content}

def resume_strategist(state: AgentState):
    print("🧠 Resume Strategist")

    prompt = f"Based on job analysis, create a tailored resume draft. Job analysis: {state['analysis']}"
    response = llm.invoke(prompt)

    return {"resume_draft": response.content}

def content_refinement(state: AgentState):
    print("✨ Refinement Agent")

    prompt = f"""
Improve clarity and structure of this resume.

Rules:
- do NOT add new facts
- improve readability
- make it professional

TEXT:
{state['resume_draft']}
"""

    response = llm.invoke(prompt)

    return {"refined_output": response.content}


graph = StateGraph(AgentState)
graph.add_node("job_analyzer", job_analyzer)
graph.add_node("resume_strategist", resume_strategist)
graph.add_node("content_refinement", content_refinement)

graph.set_entry_point("job_analyzer")
graph.add_edge("job_analyzer", "resume_strategist")
graph.add_edge("resume_strategist", "content_refinement")
graph.add_edge("content_refinement", END)

agent = graph.compile()