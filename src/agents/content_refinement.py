from src.llm import llm

def content_refinement(state):
    print("Content Refinement Agent")

    prompt = f"""
You are an elite resume writer, senior technical recruiter, and career coach.

Your task is to refine and optimize the candidate’s resume for the target job posting.

========================
TARGET JOB ANALYSIS
========================
{state.analysis}

========================
CURRENT RESUME DRAFT
========================
{state.resume_draft}

========================
STRICT RULES
========================

1. TRUTHFULNESS (HARD CONSTRAINT)
- Do NOT invent or hallucinate experience, skills, projects, or metrics.
- Only rewrite and improve existing content.

2. IMPROVEMENT GOALS
- Improve clarity, grammar, structure, and professionalism.
- Convert weak bullets into strong achievement-focused statements.
- Improve technical credibility and seniority level (without adding false claims).

3. ATS OPTIMIZATION
- Naturally integrate relevant keywords from job analysis.
- Do NOT keyword-stuff.
- Use industry-standard terminology (Cloud, Distributed Systems, DevOps, AI/ML, etc. when relevant).

4. TAILORING
- Prioritize experience relevant to the target role.
- Emphasize architecture, scalability, leadership, and system design where applicable.

5. FORMATTING (VERY IMPORTANT)
Return a resume in STRICT Markdown format with:

- Name + Title
- Contact Info
- Summary
- Skills
- Experience
- Projects (if present)
- Education
- Optional: Certifications

Each experience entry must use bullet points.

6. OUTPUT CONSTRAINT (CRITICAL)
- Output ONLY the final resume in Markdown.
- No explanations.
- No commentary.
- No preface like "Here is your resume".

========================
FINAL OUTPUT
========================
"""

    response = llm.invoke(prompt)

    return {"refined_output": response}