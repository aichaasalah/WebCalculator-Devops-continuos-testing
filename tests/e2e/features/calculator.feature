Feature: Calculator
  Scenario: Add two numbers
    Given I visit "/add/2/3"
    Then I should see "5"

  Scenario: Subtract two numbers
    Given I visit "/subtract/5/3"
    Then I should see "2"
