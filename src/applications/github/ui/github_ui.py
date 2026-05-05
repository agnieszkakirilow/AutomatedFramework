import requests
# python -m pip install selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

class GitHubUILoginPage:
    """Current class contains every UI call we use in tests"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()

    def navigate_to_page(self):
        self.driver.get('https://www.github.com/login')

    def try_to_login(self):
        # enter wrong credentils
        login_field = self.driver.find_element(By.ID, 'login_field')
        login_field.send_keys('wrong_email')
        
        pass_field = self.driver.find_element(By.CSS_SELECTOR, '#password')
        action = ActionChains(self.driver)
        action.move_to_element(pass_field).send_keys('wrong_pass')
        #pass_field.send_keys('wrong_pass')

        # click button
        pass_field_click = self.driver.find_element(By.NAME, 'commit')
        pass_field_click.click()

    def check_error_message(self):
        # check error msg
        error_msg = self.driver.find_element(By.ID, 'js-flash-container')
        print(f'error msg: {error_msg}')
        time.sleep(5)
        assert error_msg is not None

    def close_browser(self):
        self.driver.close()