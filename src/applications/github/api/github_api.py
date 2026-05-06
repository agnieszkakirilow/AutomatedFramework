# pip install requests
import requests
from src.config.config_hard import config_all

class GitHubAPIClient:
    """Current class contains every API call we use in tests"""
    
    def search_repos(self, repo_name):
        """searches for the repository and returns body
        Documentation: https://docs.github.com
        Args: repo_name: str - name of the repository
        Returns: body: .json - body of the response"""
        
        URL = config_all.__getattr__("URL")
        print(f"Sending request to url {URL}")
        response = requests.get(URL, params={'q': repo_name})
        body = response.json()
        print("Response retrieved")
        return body
    
    def search_commits(self, commit_hash):
        URL = config_all.__getattr__("URL")
        response = requests.get(URL, params={'q':commit_hash})
        print(f"sent request to {response}")
        body = response.json(0)
        print("response retrieved")
        return body