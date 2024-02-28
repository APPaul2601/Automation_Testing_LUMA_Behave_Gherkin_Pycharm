Feature: Login Page
  Background: Open login page
    Given I am on the login page

  Scenario: Check that the URL is correct
    Then The URL of the login page is "https://magento.softwaretestingboard.com/customer/account/login/"

  Scenario: Error messages for email and password
    When I press the login button until I see the errors
    Then Email error is displayed, "This is a required field."
    And Password error is displayed, "This is a required field."

  Scenario: Login with unregistered email
    When I enter "hello@yahoo.com" in the email input on the login page
    And I enter "passwoRD123" in the password input on the login page
    And I press the login button
    Then I should see the main error "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." message
