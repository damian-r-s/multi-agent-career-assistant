from state import AgentState
from tools.file_reader import read_file
from tools.github_api import fetch_github_profile
from tools.job_description_client import load_url_content

def prepare_initial_state(job_url=None, github_username=None, resume_path=None):
    state = AgentState()

    if job_url:
        print(f"Loading job posting from URL: {job_url}")
        job_content = load_url_content(job_url)
        state.job_posting = job_content
            
    if github_username:
        print(f"Fetching GitHub profile for username: {github_username}")
        github_data = fetch_github_profile(github_username)
        state.github_profile = str(github_data) if github_data else None

    if resume_path:
        print(f"Reading resume from file: {resume_path}")
        resume_data = read_file(resume_path)
        state.resume_file = resume_data

    return state