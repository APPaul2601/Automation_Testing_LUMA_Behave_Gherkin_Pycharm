from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from random import randint


class MyCartPage(BasePage):
    MAIN_PAGE_URL = "https://magento.softwaretestingboard.com/"
    PRODUCT_PRICE = (By.ID, "product-price-1316")
    INPUT_SEARCH = (By.ID, "search")
    PRODUCT = (By.CSS_SELECTOR, ".product.name.product-item-name")
    PRODUCT_CART = (By.CSS_SELECTOR, ".cart.item")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button[title='Search']")
    BUTTON_ADD_TO_CART = (By.ID, "product-addtocart-button")
    BUTTON_SHOW_CART = (By.CSS_SELECTOR, ".action.showcart")
    BUTTON_VIEW_CART = (By.CSS_SELECTOR, "[class~='viewcart']")
    ORDER_TOTAL = (By.XPATH, "//span[@class='price' and @data-bind='text: getValue()'][contains(text(), '$57.00')]")

    def open(self):
        self.driver.get(self.MAIN_PAGE_URL)

    def set_search(self, text):
        self.type(self.INPUT_SEARCH, text)

    def click_search_button(self):
        search_button = self.wait_for_element_by_value(*self.BUTTON_SEARCH)
        search_button.click()

    def click_add_to_cart_button(self):
        add_to_cart_button = self.wait_for_element_by_value(*self.BUTTON_ADD_TO_CART)
        add_to_cart_button.click()

    def click_show_cart_button(self):
        self.wait_for_pop_up_to_disappear()
        self.find(*self.BUTTON_SHOW_CART).click()

    def click_view_cart_button(self):
        view_cart_button = self.wait_for_element_to_be_clickable(self.BUTTON_VIEW_CART)
        view_cart_button.click()

    def check_number_of_elements_after_search(self, expected_num):
        product_list = self.wait_for_elements(self.PRODUCT)
        assert len(product_list) == int(
            expected_num), f"Expected {expected_num} elements, but found {len(product_list)}."

    def check_number_of_elements_in_cart(self, expected_num):
        product_list = self.wait_for_elements(self.PRODUCT_CART)
        assert len(product_list) == int(expected_num), f"Expected {expected_num} elements, but found {len(product_list)}."

    def pick_size(self):
        random_index = randint(0, 3)
        size = self.driver.find_element(By.CSS_SELECTOR, f".swatch-option.text[index='{random_index}']")
        size.click()

    def pick_color(self):
        random_index = randint(0, 1)
        color = self.driver.find_element(By.CSS_SELECTOR, f".swatch-option.color[index='{random_index}']")
        color.click()

    def get_jacket_elements(self):
        locator = (By.CSS_SELECTOR, 'strong.product.name a.product-item-link')
        return self.driver.find_element(*locator)

    def add_jacket(self):
        jacket_elements = self.get_jacket_elements()
        pick = 0
        while pick < 1:
            jacket_elements.click()
            self.pick_color()
            self.pick_size()
            self.click_add_to_cart_button()
            pick += 1
            self.driver.implicitly_wait(2)

    def order_total(self):
        return self.driver.find_element(*self.ORDER_TOTAL).text
