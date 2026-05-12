from llm import llm

def profile_builder(state):
    print("Thinking - Profile Builder")

    prompt = f"Build a professional profile based on job analysis and GitHub data. Job: {state.job_posting}, Analysis: {state.analysis}, GitHub: {state.github_profile}"
    response = llm.invoke(prompt)

    return {"profile_data": response.content}