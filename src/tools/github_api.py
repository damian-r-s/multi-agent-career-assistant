import requests

class GitHubClient:
    @staticmethod
    def fetch_github_profile(username):
        url = f"https://api.github.com/users/{username}"

        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return None