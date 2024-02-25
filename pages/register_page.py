from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    REGISTER_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    INPUT_FIRST_NAME = (By.ID, "firstname")
    INPUT_LAST_NAME = (By.ID, "lastname")
    INPUT_EMAIL = (By.ID, "email_address")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "[id='password']")
    INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[id='password-confirmation']")
    ERROR_FIRST_NAME = (By.ID, "firstname-error")
    ERROR_LAST_NAME = (By.ID, "lastname-error")
    ERROR_EMAIL = (By.ID, "email_address-error")
    ERROR_PASSWORD = (By.ID, "password-error")
    ERROR_CONFIRM_PASSWORD = (By.ID, "password-confirmation-error")
    BUTTON_REGISTER = (By.CSS_SELECTOR, ".action.submit.primary")

    def open(self):
        self.driver.get(self.REGISTER_PAGE_URL)

    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_confirm_password(self, text):
        self.type(self.INPUT_CONFIRM_PASSWORD, text)

    def click_register_button(self):
        register_button = self.wait_for_element_by_value(*self.BUTTON_REGISTER)
        register_button.click()

    def is_first_name_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_FIRST_NAME).is_displayed()
        return error

    def is_last_name_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_LAST_NAME).is_displayed()
        return error

    def is_email_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_EMAIL).is_displayed()
        return error

    def is_password_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_PASSWORD).is_displayed()
        return error

    def is_confirm_password_error_displayed(self):
        error = self.wait_for_element_by_value(*self.ERROR_CONFIRM_PASSWORD).is_displayed()
        return error

    def email_error_contains(self, text):
        return text in self.get_text(self.ERROR_EMAIL)

    def password_error_contains(self, text):
        return text in self.get_text(self.ERROR_PASSWORD)

    def confirm_password_error_contains(self, text):
        return text in self.get_text(self.ERROR_CONFIRM_PASSWORD)



