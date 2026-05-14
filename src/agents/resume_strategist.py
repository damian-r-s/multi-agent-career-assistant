from src.llm import llm

def resume_strategist(state):
    print("Thinking - Resume Strategist")

    prompt = f"Based on job analysis, create a tailored resume draft. Job analysis: {state.analysis}, Profile: {state.profile_data}"
    response = llm.invoke(prompt)

    return {"resume_draft": response.content}
