"""Stores tests related to start page"""
import logging
import random

import pytest
from selenium.webdriver.chrome import webdriver

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage():

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

    @pytest.fixture(scope="function")
    def driver(self):
        """Create and return driver, close after test"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    def test_valid_login(self, start_page):
        self.log = logging.getLogger(__name__)
        """
        - Create driver
        - Open start page
        - Find Username field
        - Put value
        - Find Password field
        - Put value
        - Find email field
        - Click on Sign In button
        - Verify approve message
        """
        # fill fields
        username_value = f"itymc{self.random_num()}"
        password_value = f"itymcPwd{self.random_num()}"
        email_value = f"itymc{self.random_num()}@ukr.net"
        main_page = start_page.register_user(username_value, password_value, email_value)
        # verify approve message

        main_page.verify_correct_login(username_value)
        self.log.info("Fields are filled")

        main_page.sign_out()
