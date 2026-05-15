from src.llm import llm

def interview_prep(state):
    print("Thinking - Interview Prep Agent")

    prompt = f"""
You are a technical recruiter and interview coach.

Create a tailored interview preparation guide based on:

JOB POSTING:
{state.job_posting}

JOB ANALYSIS:
{state.analysis}

REFINED RESUME:
{state.refined_output}

Return a structured report with:

1. Job Summary
- Key responsibilities
- Required technical + soft skills

2. Candidate Match
- Why candidate fits
- Key strengths
- Possible gaps / risks

3. Technical Questions
- 5 beginner
- 5 intermediate
- 5 advanced

For each question include:
- question
- why asked
- key points of good answer

Focus on system design, APIs, cloud, DevOps, databases, and core engineering concepts when relevant.

4. Behavioral Questions
- 5 STAR-based questions
For each:
- what is evaluated
- how to answer well

5. System Design (if relevant)
- 3 scenarios
- key topics (scalability, reliability, tradeoffs)

6. Resume Deep Dive
- 5 questions based on candidate experience (projects, decisions, tradeoffs, challenges)

7. Final Tips
- key strengths to highlight
- weaknesses framing
- 24h checklist

Rules:
- Be concise
- Avoid repetition
- Focus on practical interview readiness
"""
    response = llm.invoke(prompt)

    return {"interview_prep": response}