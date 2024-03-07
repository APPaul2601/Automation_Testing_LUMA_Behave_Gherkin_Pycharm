from browser import Browser
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.my_cart_page import MyCartPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.my_cart_page = MyCartPage()


def after_all(context):
    context.browser.close()
