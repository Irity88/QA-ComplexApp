from time import sleep

from selenium.webdriver.common.by import By

from constants.main_page import MainPageConstants
from pages.base import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def verify_correct_login(self, username):
        """verify welcome message"""
        message = self.driver.find_element(by=By.XPATH, value=self.constants.WELCOME_MESSAGE_XPATH)
        assert username in message.text

    def sign_out(self):
        self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_OUT_BUTTON_XPATH).click()
        sleep(1)
