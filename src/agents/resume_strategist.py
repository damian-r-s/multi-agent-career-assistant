from src.llm import llm

def resume_strategist(state):
    print("Thinking - Resume Strategist")

    prompt = f"""
You are a senior resume strategist and ATS optimization expert.

Create a tailored, ATS-optimized resume draft.

INPUTS:

JOB ANALYSIS:
{state.analysis}

CANDIDATE PROFILE:
{state.profile_data}

TASK:
Generate a complete resume optimized for ATS and recruiter impact.

STRUCTURE:

1. Professional Summary
- 3–5 sentences
- Aligned with target role and seniority
- Focus on technical strengths and impact

2. Core Skills
- Programming languages
- Backend / Frontend
- Cloud / DevOps / CI/CD
- Databases
- Architecture / System design
- AI/ML (if relevant)
- Security / Testing / Tools

Prioritize job-relevant skills and strongest capabilities.

3. Experience
- Polished bullet points
- Action-oriented language
- Focus: impact, ownership, scalability, systems, architecture
- No invention or fabricated metrics

Each role:
- Title + Company
- Bullet points (clear, impactful)

4. Projects (if any)
- Most relevant technical projects
- Emphasize complexity, architecture, scalability

5. Education
- Degrees and institutions

6. Certifications (if any)

7. ATS Keywords
- Extract relevant job keywords
- Integrate naturally (no stuffing)

Rules:
- Be concise and professional
- Do not invent facts or metrics
- Avoid fluff and repetition
- Make it recruiter-ready and scannable
- Output ONLY the resume
"""
    response = llm.invoke(prompt)

    return {"resume_draft": response}