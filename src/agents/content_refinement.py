from src.llm import llm

def content_refinement(state):
    print("Content Refinement Agent")

    prompt = f"""
Improve clarity and structure of this resume.

Rules:
- do NOT add new facts
- improve readability
- make it professional

TEXT:
{state.resume_draft}
"""

    response = llm.invoke(prompt)

    return {"refined_output": response.content}
