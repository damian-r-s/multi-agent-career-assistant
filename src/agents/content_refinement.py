from src.llm import llm

def content_refinement(state):
    print("Content Refinement Agent")

    prompt = f"""
You are a senior resume writer and technical recruiter.

Refine the resume for the target job.

================
JOB ANALYSIS
================
{state.analysis}

================
RESUME DRAFT
================
{state.resume_draft}

TASK:
Rewrite the resume to improve clarity, structure, and impact while strictly preserving truth.

RULES:
- Do NOT invent or add new experience, skills, or metrics.
- Improve wording, professionalism, and technical accuracy.
- Tailor content to the job (keywords, relevance, ATS optimization without stuffing).
- Emphasize architecture, scalability, leadership, and system design where relevant.

FORMAT (STRICT Markdown):
- Name + Title
- Contact Info
- Summary
- Skills
- Experience (bullet points, improved impact wording)
- Projects (if any)
- Education
- Certifications (optional)

OUTPUT RULES:
- Output ONLY the final resume in Markdown
- No explanations or commentary
"""
    response = llm.invoke(prompt)

    return {"refined_output": response}