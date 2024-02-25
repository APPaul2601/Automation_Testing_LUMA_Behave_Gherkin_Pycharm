from selenium.webdriver.common.by import By

from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(Browser):

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(*text)

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text if element else ""

    def is_url_correct(self, expected_url):
        return self.driver.current_url == expected_url

    def wait_for_element_by_value(self, by, value, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            raise TimeoutException("Timed out waiting for element")

    def wait_for_element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception("Element not found.")

    def wait_for_elements(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    def wait_for_element_to_be_clickable(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise Exception(f"Element not clickable.")

    def wait_for_pop_up_to_disappear(self):
        try:
            WebDriverWait(self.driver, 5).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page.messages"))
            )
        except TimeoutException:
            # Pop-up did not appear or did not disappear within the timeout
            pass
