from state import AgentState
from tools.file_reader import read_file
from tools.github_api import fetch_github_profile

def prepare_initial_state(job_posting, github_username=None, resume_path=None):
    state = AgentState(job_posting=job_posting)

    if github_username:
        github_data = fetch_github_profile(github_username)
        state.github_profile = str(github_data) if github_data else None

    if resume_path:
        resume_data = read_file(resume_path)
        state.resume_file = resume_data

    return state