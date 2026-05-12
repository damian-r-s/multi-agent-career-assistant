from llm import llm

def interview_prep(state):
    print("Thinking - Interview Prep Agent")

    prompt = f"Prepare interview questions and tips based on job analysis and refined resume. Job: {state.job_posting}, Analysis: {state.analysis}, Resume: {state.refined_output}"
    response = llm.invoke(prompt)

    return {"interview_prep": response.content}