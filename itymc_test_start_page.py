"""Stores tests related to start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def random_num(self):
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

    # Создать тест (поглядывая на имеющийся) который проверяет ошибку при логине с инвалидным паролем и логином.
    # (Проверка таже, добавляется только заполнение полей)

    def test_valid_login(self):
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
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value="//input[@id='username-register']")
        username.clear()
        username.send_keys(f"itymc{self.random_num()}")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value="//input[@id='password-register']")
        password.clear()
        password.send_keys(f"itymcPwd{self.random_num()}")
        # Find and clear e-mail field
        email = driver.find_element(by=By.XPATH, value="//input[@id='email-register']")
        email.clear()
        email.send_keys(f"itymc{self.random_num()}@ukr.net")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        # Click button
        sleep(3)
        button.click()
        # # Find approve message
        message = driver.find_element(by=By.XPATH, value=".//h2")
        # # Verify message
        assert "itymc" in message.text
        # Find Sign Out button
        button_sign_out = driver.find_element(by=By.XPATH, value=".//button[text()='Sign Out']")
        # Click button
        sleep(3)
        button_sign_out.click()
        sleep(3)
