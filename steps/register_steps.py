from behave import *


@given('I am on the register page')
def step_impl(context):
    context.register_page.open()


@then('The URL of the register page is "{url}"')
def step_impl(context, url):
    assert context.register_page.is_url_correct(url), "URL incorrect"


@when('I press the register button')
def step_impl(context):
    context.register_page.click_register_button()


@then('The first name error is displayed')
def step_impl(context):
    assert context.register_page.is_first_name_error_displayed()


@then('The last name error is displayed')
def step_impl(context):
    assert context.register_page.is_last_name_error_displayed()


@then('The email error is displayed')
def step_impl(context):
    assert context.register_page.is_email_error_displayed()


@then('The password error is displayed')
def step_impl(context):
    assert context.register_page.is_password_error_displayed()


@then('The password confirmation error is displayed')
def step_impl(context):
    assert context.register_page.is_confirm_password_error_displayed()


@when('I enter "{email}" in the email input on the register page')
def step_impl(context, email):
    context.register_page.set_email(email)


@then('I should see "Please enter a valid email address (Ex: johndoe@domain.com)." message')
def step_impl(context):
    assert context.register_page.is_email_error_displayed()
    assert context.register_page.email_error_contains('Please enter a valid email address (Ex: johndoe@domain.com).')


@when('I enter "{password}" in the password input')
def step_impl(context, password):
    context.register_page.set_password(password)


@when('I enter the same "{password}" in the confirm password input')
def step_impl(context, password):
    context.register_page.set_confirm_password(password)


@then('I should see "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing '
      'spaces will be ignored." message')
def step_impl(context):
    assert context.register_page.is_password_error_displayed()
    assert context.register_page.password_error_contains('Minimum length of this field must be equal or greater than '
                                                         '8 symbols. Leading and trailing spaces will be ignored.')


@then('I should see "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, '
      'Upper Case, Digits, Special Characters." message')
def step_impl(context):
    assert context.register_page.is_password_error_displayed()
    assert context.register_page.password_error_contains('Minimum of different classes of characters in password is '
                                                         '3. Classes of characters: Lower Case, Upper Case, Digits, '
                                                         'Special Characters.')


@when('I enter a different "{confirm_password}" in the confirm password input')
def step_impl(context, confirm_password):
    context.register_page.set_confirm_password(confirm_password)


@then('I should see "Please enter the same value again." message')
def step_impl(context):
    assert context.register_page.is_confirm_password_error_displayed()
    assert context.register_page.confirm_password_error_contains('Please enter the same value again.')
