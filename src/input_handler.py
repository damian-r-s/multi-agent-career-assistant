from src.state import AgentState
from src.tools.file_reader import CvFileReader
from src.tools.github_api import GitHubClient
from src.tools.job_client import JobsReaderClient

def prepare_initial_state(job_url=None, github_username=None, resume_path=None):
    state = AgentState()

    if job_url:
        print(f"Loading job posting from URL: {job_url}")
        job_content = JobsReaderClient.load_url_content(job_url)
        state.job_posting = job_content
            
    if github_username:
        print(f"Fetching GitHub profile for username: {github_username}")
        github_data = GitHubClient.fetch_github_profile(github_username)
        state.github_profile = str(github_data) if github_data else None

    if resume_path:
        print(f"Reading resume from file: {resume_path}")
        resume_data = CvFileReader.read(resume_path)
        state.resume_file = resume_data

    return state
