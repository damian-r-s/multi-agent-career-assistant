from src.llm import llm

def profile_builder(state):
    print("Thinking - Profile Builder")

    prompt = f"""
You are a technical recruiter and career strategist.

Build a concise professional candidate profile for the target role.

INPUTS:

JOB POSTING:
{state.job_posting}

JOB ANALYSIS:
{state.analysis}

GITHUB DATA:
{state.github_profile}

Return structured profile:

1. Professional Summary
- 3–5 sentence summary aligned with target role
- Highlight strongest engineering strengths
- Match seniority to job

2. Core Skills (categorized)
- Programming languages
- Backend / Frontend
- Cloud / DevOps
- Databases
- Architecture / System design
- AI/ML or Data (if relevant)

Include inferred proficiency only when clear.

3. Key Strengths
- 5–8 strongest engineering capabilities
- Focus on: scalability, systems, backend, cloud, performance, leadership

4. GitHub Insights
- Most relevant projects (max 3–5)
- Technical complexity level
- Key technologies used
- Engineering maturity signals

5. Gaps / Risks
- Missing or weak skills vs job requirements
- Potential interview concerns

6. Positioning Strategy
- How candidate should present themselves
- Top 3 selling points

7. ATS Keywords
- Key technologies
- Architecture terms
- Relevant engineering phrases

Rules:
- Be concise and specific
- No fabrication
- Focus on job relevance
"""
    response = llm.invoke(prompt)

    return {"profile_data": response}