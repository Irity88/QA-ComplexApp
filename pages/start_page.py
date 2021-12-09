from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def register_user(self, username_value, password_value, email_value):
        """Register user using provided data"""
        # fill user
        self.fill_filed(by=By.XPATH, locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username_value)
        # fill password
        self.fill_filed(by=By.XPATH, locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password_value)
        # fill email
        self.fill_filed(by=By.XPATH, locator=self.constants.SIGN_IN_EMAIL_XPATH, value=email_value)
        self.log.debug("Fields are filled with valid values")
        sleep(3)

        # Click Sign In button
        self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_BUTTON_XPATH).click()
        sleep(3)
        self.log.debug("Clicked on Sign In")
        from pages.main_page import MainPage
        return MainPage(self.driver)
