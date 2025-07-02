Feature: Shopping Cart
  In order to shop effectively
  As a customer
  I want to add and remove items, and calculate the total with discounts

  @scenario_outline
  Scenario Outline: Add items and calculate total
    Given a new shopping cart
    When I add <quantity> items with price <unitPrice>
    Then the total should be <expectedTotal>

    Examples:
      | quantity | unitPrice | expectedTotal |
      | 1        | 9.99      | 9.99          |
      | 2        | 5.50      | 11.00         |
      | 3        | 3.33      | 9.99          |

  @advanced
  Scenario: Discount applied with multiple items
    Given a new shopping cart with items:
      | quantity | price |
      | 1        | 10.00 |
      | 2        | 15.00 |
    When I apply a discount of 10%
    Then the total should be 31.50