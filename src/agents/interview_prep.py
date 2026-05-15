from src.llm import llm

def interview_prep(state):
    print("Thinking - Interview Prep Agent")

    prompt = f"""
You are an expert technical recruiter, hiring manager, and interview coach.

Your task is to prepare a comprehensive interview preparation guide tailored specifically to the candidate and the target job posting.

Use the following inputs:

JOB POSTING:
{state.job_posting}

JOB ANALYSIS:
{state.analysis}

REFINED RESUME:
{state.refined_output}

Generate a structured interview preparation report with the following sections:

1. Job Summary
- Briefly summarize the role and its key responsibilities.
- Identify the most important technical and soft skills required.

2. Candidate Match Analysis
- Explain why the candidate is a strong fit for the role.
- Highlight strengths aligned with the position.
- Identify potential weaknesses or missing experience that could be questioned during the interview.

3. Technical Interview Questions
Generate:
- 10 beginner-level questions
- 10 intermediate-level questions
- 10 advanced-level questions

Requirements:
- Questions must be highly relevant to the technologies, architecture, and responsibilities mentioned in the job posting.
- Include questions related to system design, scalability, APIs, cloud, DevOps, security, testing, databases, and software engineering best practices when applicable.
- Include behavioral and problem-solving aspects where appropriate.

For each question provide:
- The question
- Why the interviewer asks it
- What a strong answer should include
- Example answer points

4. Behavioral Interview Questions
Generate 10 behavioral questions using STAR methodology principles.

For each question provide:
- What the interviewer evaluates
- Tips for answering effectively
- Example structure for the response

5. System Design / Architecture Preparation
If relevant to the role:
- Generate 5 realistic system design interview scenarios.
- Explain what topics the candidate should discuss.
- Include scalability, reliability, observability, security, distributed systems, and tradeoffs where relevant.

6. Coding Interview Preparation
If relevant:
- List likely coding interview topics.
- Recommend algorithms, data structures, or coding patterns to review.
- Mention common mistakes candidates make.

7. Resume Deep-Dive Questions
Generate questions specifically based on the candidate's resume and experience.
Focus on:
- Previous projects
- Technical decisions
- Leadership
- Tradeoffs
- Challenges
- Achievements
- Production incidents
- Performance optimization
- Collaboration

8. Interview Strategy
Provide:
- Key talking points the candidate should emphasize
- How to present strengths confidently
- How to address weaknesses professionally
- Tips for remote interviews
- Tips for salary discussions
- Questions the candidate should ask the interviewer

9. Final Preparation Checklist
Create a concise checklist for the final 24 hours before the interview.

Formatting requirements:
- Use clear headings
- Use bullet points
- Make the content practical and specific
- Avoid generic advice
- Tailor everything to the provided job posting and resume
"""
    response = llm.invoke(prompt)

    return {"interview_prep": response}
