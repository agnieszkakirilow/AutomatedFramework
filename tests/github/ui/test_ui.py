from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from src.applications.github.ui.github_ui import GitHubUILoginPage
from src.helpers.browser_providers import BrowserProvider
from src.config.config_hard import config_all

@pytest.fixture
def github_login():
    # tearup for each
    
    driver = BrowserProvider.get_driver(config_all.__getattr__("BROWSER"))
    github_login_page = GitHubUILoginPage(driver)
    github_login_page.navigate_to_page()

    yield github_login_page
    
    #teardown for each
    github_login_page.close_browser()

def test_github_login_negative_page_obj(github_login):
    #github login wrong SELENIUM
    
    # enter wrong credentils
    github_login.try_to_login()
    
    # check error msg
    github_login.check_error_message()


