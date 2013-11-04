Feature: Basic front page

  Scenario: Latest story appears first
    Given the site contains an article
    And that article has headline "This is a test article"
    And that article has id 1
    When I visit "/"
    Then the first headline should be "This is a test article"
