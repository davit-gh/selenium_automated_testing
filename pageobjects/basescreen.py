from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseScreen(object):
    """Base class for other Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.title = driver.instance.title

    def select_element(self, locator):
        """Select an element by waiting for it to become visible"""
        wait = WebDriverWait(self.driver.instance, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def wait_until_clickable(self, locator):
        wait = WebDriverWait(self.driver.instance, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    def page_title_equals_to(self, title):
        assert self.title == title

    def take_screenshot(self):
        """Take a screenshot with a defined name based on the time and the browser"""
        millis = int(round(time.time() * 1000))
        if self.driver.name:
            driver_name = self.driver.name
        else:
            driver_name = ""
        self.driver.save_screenshot("screenshots/{}-{}-screenshots.png".format(driver_name, millis))
