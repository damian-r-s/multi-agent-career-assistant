from src.llm import llm

def profile_builder(state):
    print("Thinking - Profile Builder")

    prompt = f"""
You are an expert technical recruiter, career strategist, and personal branding specialist.

Your task is to build a professional candidate profile based on:
- the target job posting,
- the job analysis,
- and the candidate's GitHub profile data.

The output will later be used for:
- resume generation,
- interview preparation,
- ATS optimization,
- candidate positioning,
- and professional branding.

INPUT DATA

JOB POSTING:
{state.job_posting}

JOB ANALYSIS:
{state.analysis}

GITHUB PROFILE DATA:
{state.github_profile}

Generate a comprehensive professional profile with the following sections:

1. Professional Summary
Create a concise but impactful professional summary that:
- aligns with the target role,
- highlights technical strengths,
- emphasizes relevant engineering experience,
- reflects seniority appropriately,
- sounds professional and recruiter-friendly.

2. Core Technical Skills
Categorize skills into sections such as:
- Programming Languages
- Frameworks & Libraries
- Cloud & Infrastructure
- Databases
- DevOps & CI/CD
- APIs & Integration
- Architecture & Design
- AI/ML & Data Engineering
- Testing & Quality
- Security
- Tools & Platforms

For each category:
- identify strongest areas,
- estimate proficiency level when inferable,
- prioritize skills relevant to the job posting.

3. Engineering Strengths
Identify likely strengths such as:
- backend engineering,
- distributed systems,
- cloud engineering,
- DevOps,
- architecture,
- performance optimization,
- scalability,
- automation,
- leadership,
- open-source contribution,
- system reliability,
- AI/ML engineering,
- blockchain/Web3,
- frontend engineering,
- data engineering,
etc.

4. GitHub Project Analysis
Analyze the GitHub data and identify:
- most impressive projects,
- technical complexity,
- engineering maturity,
- coding patterns,
- architecture quality,
- technologies frequently used,
- evidence of collaboration,
- production-readiness signals,
- testing quality,
- documentation quality.

5. Candidate Positioning
Explain how the candidate should position themselves for this role:
- strongest selling points,
- differentiators,
- niche expertise,
- leadership potential,
- technical depth,
- business impact.

6. Potential Concerns or Gaps
Identify:
- missing skills,
- weak areas,
- technologies absent from profile,
- areas likely to be questioned during interviews.

Provide constructive recommendations for improvement.

7. Recommended Resume Focus
Suggest:
- which skills to highlight first,
- which projects deserve emphasis,
- what accomplishments should be prioritized,
- what keywords should appear prominently.

8. Interview Preparation Insights
Predict:
- likely interview focus areas,
- strengths the candidate should emphasize,
- technical topics worth reviewing before interviews.

9. ATS Optimization Keywords
Generate:
- high-value ATS keywords,
- technical phrases,
- architecture terminology,
- engineering buzzwords relevant to the role.

10. Overall Candidate Assessment
Provide:
- estimated seniority level,
- overall marketability,
- fit for the role,
- competitiveness level,
- likely recruiter perception.

Important Rules:
- Do NOT invent fake experience or achievements.
- Infer carefully and conservatively.
- Be specific and technically accurate.
- Prioritize relevance to the target job posting.
- Avoid generic career advice.
- Use clean formatting and clear section headings.
"""

    response = llm.invoke(prompt)

    return {"profile_data": response}