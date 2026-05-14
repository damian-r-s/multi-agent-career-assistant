def job_analyzer(state):
    print("Thinking - Job Analyzer")

    prompt = f"""
You are an expert technical recruiter, hiring manager, and career analyst.

Analyze the following job posting in depth and extract structured insights that will help:
- tailor a resume,
- prepare for interviews,
- identify skill gaps,
- optimize candidate positioning.

JOB POSTING:
{state.job_posting}

Generate a detailed analysis with the following sections:

1. Role Summary
- Brief description of the role
- Main responsibilities
- Seniority level
- Type of candidate the company is likely seeking

2. Required Technical Skills
Extract and categorize:
- Programming languages
- Frameworks/libraries
- Cloud technologies
- Databases
- DevOps tools
- Infrastructure/platforms
- APIs/integration technologies
- Architecture patterns
- Testing tools
- Security requirements
- AI/ML/Data technologies if mentioned

For each skill:
- Mention importance level:
  - Critical
  - Important
  - Nice-to-have

3. Soft Skills & Business Expectations
Identify:
- Communication expectations
- Leadership expectations
- Team collaboration
- Ownership/accountability
- Problem-solving expectations
- Stakeholder interaction

4. Experience Requirements
Extract:
- Years of experience
- Industry/domain experience
- Leadership/team lead expectations
- Enterprise/system scale expectations
- Production support expectations

5. Hidden Expectations (Important)
Infer likely unstated expectations such as:
- Fast-paced environment
- Startup mentality
- Banking/regulated environment
- Scalability experience
- High availability systems
- CI/CD maturity
- Agile/Scrum culture
- Client-facing responsibilities

6. Key Resume Keywords
Generate:
- ATS-friendly keywords
- Important phrases
- Action verbs
- Technologies to emphasize

7. Interview Focus Areas
Predict likely interview topics:
- Technical areas
- System design topics
- Coding topics
- Behavioral areas
- Architecture discussions
- DevOps/cloud discussions

8. Candidate Evaluation Criteria
Explain:
- What will most likely impress interviewers
- What weaknesses may eliminate candidates
- What differentiates top candidates

9. Recommended Resume Positioning
Suggest:
- Which skills should be highlighted first
- Which experience should be emphasized
- What achievements would best match the role

10. Overall Difficulty Assessment
Provide:
- Estimated interview difficulty
- Market competitiveness
- Recommended preparation depth

Formatting requirements:
- Use structured headings
- Use bullet points
- Be highly specific
- Avoid generic advice
- Infer missing context intelligently
"""

    response = llm.invoke(prompt)

    return {"analysis": response.content}