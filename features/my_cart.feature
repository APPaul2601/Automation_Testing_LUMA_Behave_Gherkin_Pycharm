Feature: Add to cart and see the Checkout price

  Scenario Outline: Check that there are enough elements on the page after a search
    Given I am on the main page
    When I enter "<search_term>" in the search input
    And I press the search button
    Then I should see "<expected_count>" elements
    Examples:
      | search_term | expected_count |
      | jacket      | 12             |

  Scenario Outline: Add 1 jacket to the cart
    Given I am on the main page
    When I enter "jacket" in the search input
    And I press the search button
    And I add the first jacket
    And I go to my cart page
    Then I should have "<expected_count>" jacket in the cart
    And The total price should be "<expected_total>"
    Examples:
      | expected_total | expected_count |
      | 57.00       | 1                 |