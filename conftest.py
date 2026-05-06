# without it you have to run python -m pytest . instead of pytest .
import pytest
from src.applications.github.api.github_api import GitHubAPIClient
# pip install pytest
# python -m pytest .

@pytest.fixture
def git_hub_api_app():
    # before each test pre test steps
    print("Entering git_hub_api_app")
    github_api_client = GitHubAPIClient()

    yield github_api_client

    # post test steps
    print("Executed even when assertion fails")
