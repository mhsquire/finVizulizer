

Feature: Financial Data
  Running the program causes it to grab latest financial data.

  Scenario: a successful connection
    When a request for financial data is made
    Then connection is ok

  Scenario: presence of financial data
    Given a successful connection is established
    When a request for financial data is made
    Then data is present
