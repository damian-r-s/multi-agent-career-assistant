from src.llm import llm

def job_analyzer(state):
    print("Thinking - Job Analyzer")

    prompt = f"Extract key skills and requirements from this job: {state.job_posting}"
    response = llm.invoke(prompt)

    return {"analysis": response.content}
