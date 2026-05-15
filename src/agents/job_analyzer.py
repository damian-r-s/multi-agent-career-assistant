from src.llm import llm

def job_analyzer(state):
    print("Thinking - Job Analyzer")

    prompt = f"""
You are a senior technical recruiter.

Analyze this job posting and extract structured insights for resume tailoring and interview prep.

JOB POSTING:
{state.job_posting}

Return a structured analysis:

1. Role Summary
- Role overview
- Responsibilities
- Seniority level
- Target candidate profile

2. Key Skills (grouped)
Categorize and rate importance:
- Programming languages
- Frameworks
- Cloud / DevOps
- Databases
- Architecture / System design
- Security / Testing
- Domain-specific tech (if any)

Use: Critical / Important / Nice-to-have

3. Soft Skills
- Communication
- Leadership
- Ownership
- Collaboration
- Problem-solving

4. Experience Requirements
- Years of experience
- Domain / industry
- Scale / production expectations
- Leadership expectations

5. Interview Focus
- Technical areas
- System design topics
- Coding topics
- Behavioral focus

6. Resume Keywords
- ATS keywords
- Important phrases
- Key technologies

7. Hiring Signals
- Likely hidden expectations
- Environment type (startup, enterprise, regulated, etc.)

Rules:
- Be specific and practical
- Avoid generic statements
- Infer only from context
"""
    response = llm.invoke(prompt)

    return {"analysis": response}