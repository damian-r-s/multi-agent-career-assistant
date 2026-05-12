from state import AgentState
import graph

if __name__ == "__main__":
    initial_state = AgentState(
        job_posting="We are looking for a software engineer with experience in Python, machine learning, and cloud computing.",
        analysis=None,
        resume_draft=None,
        refined_output=None
    )

    final_state = graph.agent.run(initial_state)

    print("\nFinal Refined Resume:\n", final_state['refined_output'])