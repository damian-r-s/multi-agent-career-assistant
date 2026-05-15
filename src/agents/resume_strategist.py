from src.llm import llm

def resume_strategist(state):
    print("Thinking - Resume Strategist")

    prompt = f"""
You are an elite resume strategist, technical recruiter, ATS optimization expert, and executive career coach.

Your task is to create a highly tailored, professional, ATS-optimized resume draft based on:
- the target job analysis,
- and the candidate professional profile.

The goal is to maximize:
- interview invitations,
- ATS matching,
- recruiter attention,
- technical credibility,
- and alignment with the target role.

INPUT DATA

JOB ANALYSIS:
{state.analysis}

CANDIDATE PROFILE:
{state.profile_data}

Generate a complete professional resume draft with the following structure:

1. Professional Summary
Create a strong summary that:
- aligns with the target role,
- highlights seniority appropriately,
- emphasizes relevant technical expertise,
- demonstrates business impact,
- sounds confident and professional,
- is concise and recruiter-friendly.

2. Core Skills
Organize skills into professional categories such as:
- Programming Languages
- Frameworks & Libraries
- Cloud & Infrastructure
- DevOps & CI/CD
- Databases
- APIs & Integration
- Architecture & Design
- AI/ML & Data Engineering
- Security
- Testing & Automation
- Tools & Platforms

Prioritize:
- technologies mentioned in the job posting,
- strongest candidate skills,
- ATS relevance.

3. Professional Experience
Generate polished experience sections with:
- strong action verbs,
- achievement-oriented bullet points,
- technical depth,
- business impact,
- scalability and architecture focus where relevant,
- leadership and ownership emphasis when applicable.

Requirements:
- Keep all statements factually grounded in the provided profile.
- Do NOT invent companies, positions, or fake metrics.
- Improve phrasing and presentation professionally.
- Emphasize production systems, cloud, DevOps, distributed systems, AI/ML, scalability, automation, and architecture when relevant to the role.

Each experience section should include:
- role/title,
- company,
- timeframe if available,
- concise but impactful bullet points.

4. Projects Section
If project information exists:
- highlight technically impressive projects,
- emphasize engineering complexity,
- architecture,
- scalability,
- automation,
- open-source contributions,
- AI/ML or distributed systems work where applicable.

5. Education
Include:
- degrees,
- universities,
- relevant academic focus.

6. Certifications & Courses
If available:
- include relevant certifications,
- technical training,
- advanced courses.

7. ATS Optimization
Naturally incorporate:
- keywords from the job analysis,
- important engineering terminology,
- role-specific language,
- cloud/platform/tool terminology.

8. Formatting Rules
- Use clean markdown formatting.
- Use concise professional language.
- Avoid fluff and generic statements.
- Avoid keyword stuffing.
- Make the resume highly scannable.
- Use bullet points consistently.
- Keep strong visual structure.

9. Strategic Positioning
The resume should position the candidate as:
- highly relevant for the target role,
- technically strong,
- experienced with modern engineering practices,
- capable of ownership and delivery,
- credible for senior-level interviews.

Output Requirements:
- Return ONLY the resume.
- Do NOT include explanations.
- Do NOT include commentary outside the resume.
"""

    response = llm.invoke(prompt)

    return {"resume_draft": response}