import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)

    def fill_filed(self, by, locator, value):
        """Fill field using  variables"""
        username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)
