from conftest import git_hub_api_app


def test_search_for_existing_repo(git_hub_api_app):
    existing_repo_name = 'sergii'
    repos = git_hub_api_app.search_repos(existing_repo_name)
    
    print('Checking total count is not zero')
    assert repos['total_count'] != 0

def test_search_for_nonexisting_repo(git_hub_api_app):
    nonexisting_repo_name = 'afdklahflal'
    repos = git_hub_api_app.search_repos(nonexisting_repo_name)
    
    print('Checking total count is zero')
    assert repos['total_count'] == 0

