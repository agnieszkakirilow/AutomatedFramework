import requests
# python -m pip install selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
from src.applications.github.ui.github_ui import GitHubUILoginPage

@pytest.fixture
def github_login():
    # tearup for each
    github_login_page = GitHubUILoginPage()
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


