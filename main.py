from state import AgentState
from input_handler import prepare_initial_state
import graph

if __name__ == "__main__":   
    
    job_url = "https://www.google.com/about/careers/applications/jobs/results/122028489434899142-senior-software-engineer-operations-research?location=Zurich%2C%20Switzerland"    
    github_username = "damian-r-s"
    resume_path = "test/example-resume.txt"

    initial_state = prepare_initial_state(        
        job_url=job_url,
        github_username=github_username,
        resume_path=resume_path
    )

    final_state = graph.agent.invoke(initial_state)

    print("\nFinal Refined Resume:\n", final_state['refined_output'])
    print("\nInterview Prep:\n", final_state['interview_prep'])