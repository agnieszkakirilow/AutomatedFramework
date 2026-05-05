import pytest
from src.applications.github.api.github_api import GitHubAPIClient
# pip install pytest
# python -m pytest .

def test_search_for_existing_repo():
    github_api_client = GitHubAPIClient()
    existing_repo_name = 'sergii'
    repos = github_api_client.search_repos(existing_repo_name)
    
    print('Checking total count is not zero')
    assert repos['total_count'] != 0

def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPIClient()
    nonexisting_repo_name = 'afdklahflal'
    repos = github_api_client.search_repos(nonexisting_repo_name)
    
    print('Checking total count is zero')
    assert repos['total_count'] == 0

def test_search_for_existing_commits():
    github_api_client = GitHubAPIClient()
    commit_hash = 'afdklahflal'
    repos = github_api_client.search_repos(commit_hash)
    
    print('Checking total count is zero')
    assert repos['total_count'] == 0