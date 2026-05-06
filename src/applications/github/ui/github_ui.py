import requests
# python -m pip install selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from src.applications.github.ui.base_page import BasePage
import pytest

class GitHubUILoginPage(BasePage):
    """Current class contains every UI call we use in tests"""
    
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_page(self):
        self.driver.get('https://www.github.com/login')
    
    def try_to_login(self):
        # enter wrong credentils
        login_field = self.find_el(By.ID, 'login_field')
        login_field.send_keys('wrong_email')
        
        pass_field = self.find_el(By.CSS_SELECTOR, '#password')
        action = ActionChains(self.driver)
        action.move_to_element(pass_field).send_keys('wrong_pass')

        # click button
        self.click_el(By.NAME, 'commit')

    def check_error_message(self):
        # check error msg
        error_msg = self.find_el(By.ID, 'js-flash-container')
        print(f'error msg: {error_msg}')
        time.sleep(5)
        assert error_msg is not None

    def close_browser(self):
        self.driver.close()