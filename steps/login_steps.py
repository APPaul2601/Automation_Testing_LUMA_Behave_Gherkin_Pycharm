from behave import *


@given('I am on the login page')
def step_impl(context):
    context.login_page.open()


@then('The URL of the login page is "{url}"')
def step_impl(context, url):
    assert context.login_page.is_url_correct(url), "URL incorrect"


@when('I press the login button until I see the errors')
def step_impl(context):
    context.login_page.click_for_login_error()


@then('Email error is displayed, "{error}"')
def step_impl(context, error):
    assert context.login_page.is_email_error_displayed()
    assert context.login_page.email_error_contains(error)


@then('Password error is displayed, "{error}"')
def step_impl(context, error):
    assert context.login_page.is_password_error_displayed()
    assert context.login_page.password_error_contains(error)


@when('I enter "hello@yahoo.com" in the email input on the login page')
def step_impl(context):
    context.login_page.set_email('hello@yahoo.com')


@when('I enter "passwoRD123" in the password input on the login page')
def step_impl(context):
    context.login_page.set_password('passwoRD123')


@when('I press the login button')
def step_impl(context):
    context.login_page.click_button()


@then('I should see the main error "{error}" message')
def step_impl(context, error):
    assert context.login_page.is_main_error_displayed()
    assert context.login_page.main_error_contains(error)
