# pip install requests
import requests
from src.config.config_hard import config_all
class GitHubAPIClient:
    """Current class contains every API call we use in tests"""
    
    def __init__(self):
        pass

    def search_repos(self, repo_name):
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