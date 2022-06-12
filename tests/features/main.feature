

Feature: Financial Data
  Running the program causes it to grab latest financial data.

  Scenario: a successful connection has parseable data
    When a request for financial data is made
    Then connection is ok