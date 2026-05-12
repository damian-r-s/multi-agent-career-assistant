from state import AgentState
from input_handler import prepare_initial_state
import graph

if __name__ == "__main__":
    # Example inputs
    job_posting = "We are looking for a software engineer with experience in Python, machine learning, and cloud computing."
    github_username = None  # e.g., "damian-r-s"
    resume_path = None  # e.g., "resume.txt"

    initial_state = prepare_initial_state(job_posting, github_username, resume_path)

    final_state = graph.agent.invoke(initial_state)

    print("\nFinal Refined Resume:\n", final_state['refined_output'])
    print("\nInterview Prep:\n", final_state['interview_prep'])