from behave import *


@given('I am on the main page')
def step_impl(context):
    context.my_cart_page.open()


@when('I enter "{search_term}" in the search input')
def step_impl(context, search_term):
    context.my_cart_page.set_search(search_term)


@when('I press the search button')
def step_impl(context):
    context.my_cart_page.click_search_button()


@then('I should see "{expected_count}" elements')
def step_impl(context, expected_count):
    context.my_cart_page.check_number_of_elements_after_search(expected_count)


@when('I add the first jacket')
def step_impl(context):
    context.my_cart_page.add_jacket()


@when('I go to my cart page')
def step_impl(context):
    context.my_cart_page.click_show_cart_button()
    context.my_cart_page.click_view_cart_button()


@then('I should have "{expected_count}" jacket in the cart')
def step_impl(context, expected_count):
    context.my_cart_page.check_number_of_elements_in_cart(expected_count)


@then('The total price should be "{expected_total}"')
def step_impl(context, expected_total):
    order_total = float(context.my_cart_page.order_total().replace('$', ''))
    assert order_total == float(expected_total), f"Expected total: {expected_total}, Actual total: {order_total}"