Feature: Registration Page
  Background: Open register page
    Given I am on the register page

  Scenario: Check that the URL is correct
    Then The URL of the register page is "https://magento.softwaretestingboard.com/customer/account/create/"

  Scenario: Check that trying to register without completing mandatory fields displays errors
    When I press the register button
    Then The first name error is displayed
    And The last name error is displayed
    And The email error is displayed
    And The password error is displayed
    And The password confirmation error is displayed

  Scenario Outline: Register with invalid email displays the error
    When I enter "<email>" in the email input on the register page
    And I press the register button
    Then I should see this email error "Please enter a valid email address (Ex: johndoe@domain.com)." message
    Examples:
      | email |
      | pyta10        |
      | 122           |
      | pyta10@.com   |

    Scenario Outline: Register with a weak password displays the error
      When I enter "<password>" in the password input
      And I enter the same "<password>" in the confirm password input
      And I press the register button
      Then I should see this password error "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored." message
      Examples:
        | password |
        | 12345    |
        | asdf5    |

  Scenario Outline: Register without the minimum of different classes of characters displays the error
      When I enter "<password>" in the password input
      And I enter the same "<password>" in the confirm password input
      And I press the register button
      Then I should see this password error "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters." message
      Examples:
        | password |
        | 12345678      |
        | asdfghjk      |

    Scenario Outline: Register with different passwords displays the error
      When I enter "<password>" in the password input
      And I enter a different "<confirm_password>" in the confirm password input
      And I press the register button
      Then "Please enter the same value again." message should be displayed
      Examples:
        | password | confirm_password |
        | Pyta@123 | PytA@123         |
        | 123Paul! | 345pauL@         |
