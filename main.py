from state import AgentState
from input_handler import prepare_initial_state
import graph

if __name__ == "__main__":
    # Example inputs
    # Option 1: Direct job posting text
    job_posting = "We are looking for a software engineer with experience in Python, machine learning, and cloud computing."

    # Option 2: Load from URL (requires TAVILY_API_KEY)
    job_url = "https://example.com/job-posting"

    # Option 3: Load from GitHub profile
    github_username = None  # e.g., "damian-r-s"

    # Option 4: Load from resume file
    resume_path = None  # e.g., "resume.txt"

    initial_state = prepare_initial_state(        
        job_url=job_url,  # Uncomment to use URL
        github_username=github_username,
        resume_path=resume_path
    )

    final_state = graph.agent.invoke(initial_state)

    print("\nFinal Refined Resume:\n", final_state['refined_output'])
    print("\nInterview Prep:\n", final_state['interview_prep'])