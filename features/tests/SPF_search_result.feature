
Feature: Search result
  Scenario: Verify search result show the right result
    Given Open main page
    When From page header, click "Search"
    And Search for the SPF
    Then Verify the results have SPF