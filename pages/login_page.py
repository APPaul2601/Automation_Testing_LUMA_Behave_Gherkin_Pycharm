from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "pass")
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".action.login")
    ERROR_MESSAGE_EMAIL = (By.ID, "email-error")
    ERROR_MESSAGE_PASSWORD = (By.ID, "pass-error")
    ERROR_MAIN = (By.CSS_SELECTOR, ".message-error")

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_until(self, *args, max_attempts=5):
        attempts = 0

        while attempts < max_attempts:
            try:
                button = self.find(*args)
                button.click()

                WebDriverWait(self.driver, 2).until(
                    EC.visibility_of_element_located(self.ERROR_MESSAGE_EMAIL))
                WebDriverWait(self.driver, 2).until(
                    EC.visibility_of_element_located(self.ERROR_MESSAGE_PASSWORD))

                return button

            except TimeoutException:
                print("Timeout waiting for element.")
                attempts += 1

        raise TimeoutException(f"Max attempts reached. Element not found with {args}")

    def click_for_login_error(self):
        self.click_until(*self.BUTTON_LOGIN)

    def click_button(self):
        login_button = self.wait_for_element_by_value(*self.BUTTON_LOGIN)
        login_button.click()

    def is_email_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_MESSAGE_EMAIL).is_displayed()
        return error

    def is_password_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_MESSAGE_PASSWORD).is_displayed()
        return error

    def is_main_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_MAIN).is_displayed()
        return error

    def email_error_contains(self, text):
        return text in self.get_text(self.ERROR_MESSAGE_EMAIL)

    def password_error_contains(self, text):
        return text in self.get_text(self.ERROR_MESSAGE_PASSWORD)

    def main_error_contains(self, text):
        return text in self.get_text(self.ERROR_MAIN)
