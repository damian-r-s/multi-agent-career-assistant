from state import AgentState
import graph

if __name__ == "__main__":
    
    result = graph.agent.invoke({
        "job_posting": "Senior Python Engineer"
    })

    print("\nFinal Refined Resume:\n", result['refined_output'])