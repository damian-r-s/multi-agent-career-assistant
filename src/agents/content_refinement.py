from src.llm import llm

def content_refinement(state):
    print("Content Refinement Agent")

    prompt = f"""
You are an elite resume writer, technical recruiter, and executive career coach.

Your task is to refine and optimize the candidate's resume for the target job posting while preserving factual accuracy.

TARGET JOB ANALYSIS:
{state.analysis}

CURRENT RESUME DRAFT:
{state.resume_draft}

Requirements:

1. Preserve Truthfulness
- Do NOT invent experience, skills, projects, certifications, or achievements.
- Do NOT exaggerate responsibilities.
- Keep all information factually accurate.

2. Improve Professional Quality
Enhance:
- clarity
- structure
- grammar
- readability
- professionalism
- technical presentation
- impact of achievements

3. Optimize for ATS (Applicant Tracking Systems)
- Naturally incorporate relevant keywords from the job analysis.
- Improve keyword alignment without keyword stuffing.
- Use industry-standard terminology.

4. Improve Resume Impact
- Rewrite weak bullet points into strong achievement-oriented statements.
- Use strong action verbs.
- Emphasize measurable impact where information already exists.
- Improve technical credibility.

5. Tailor Resume Toward the Job
Based on the job analysis:
- Prioritize the most relevant skills and experiences.
- Highlight technologies and responsibilities aligned with the role.
- Emphasize leadership, architecture, scalability, cloud, DevOps, AI/ML, or distributed systems experience when relevant.
- Align wording with the employer’s expectations.

6. Improve Technical Sections
When applicable:
- Organize technologies into meaningful categories.
- Improve project descriptions.
- Clarify architecture and engineering contributions.
- Emphasize production-scale systems and business impact.

7. Maintain Clean Formatting
- Use concise and professional formatting.
- Use bullet points.
- Keep sections easy to scan.
- Avoid unnecessary buzzwords and fluff.
- Avoid repetition.

8. Output Requirements
Return:
- A fully refined professional resume
- Clean markdown formatting
- Clearly separated sections
- No explanations outside the resume itself

The final result should look like a polished resume prepared by a top-tier professional resume writer for a highly competitive technical role.
"""

    response = llm.invoke(prompt)

    return {"refined_output": response.content}