from langgraph.graph import StateGraph, END
from llm import llm
from state import AgentState
from agents.job_analyzer import job_analyzer
from agents.profile_builder import profile_builder
from agents.resume_strategist import resume_strategist
from agents.content_refinement import content_refinement
from agents.interview_prep import interview_prep

graph = StateGraph(AgentState)
graph.add_node("job_analyzer", job_analyzer)
graph.add_node("profile_builder", profile_builder)
graph.add_node("resume_strategist", resume_strategist)
graph.add_node("content_refinement", content_refinement)
graph.add_node("interview_prep", interview_prep)

graph.set_entry_point("job_analyzer")
graph.add_edge("job_analyzer", "profile_builder")
graph.add_edge("job_analyzer", "resume_strategist")
graph.add_edge("profile_builder", "content_refinement")
graph.add_edge("resume_strategist", "content_refinement")
graph.add_edge("content_refinement", "interview_prep")
graph.add_edge("interview_prep", END)

agent = graph.compile()