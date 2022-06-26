

Feature: Financial Data
  Running the program causes it to grab latest financial data.

  Scenario: a successful connection has parseable data
    When a request for financial data is made
    Then connection is ok

  Scenario: data can be parsed
    Given a response has been sent
    When the response is parsed
    Then the resulting table records date
    And the resulting table records time
    And the resulting table records the headline
    And the resulting table records article link