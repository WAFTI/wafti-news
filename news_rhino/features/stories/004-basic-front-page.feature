# See https://github.com/WAFTI/wafti-news/issues/3
Feature: Basic front page

  Scenario: Only story appears on front page
    Given the site contains an article
    And that article has headline "This is a test article"
    And that article has id 1
    When I visit "/news/"
    Then the first headline should be "This is a test article"

  Scenario: Latest story appears first amongst other stories
    Given the site contains 3 basic articles added in date order
    When I visit "/news/"
    Then the 1st headline should match the 3rd article
    And the 2nd headline should match the 2nd article
    And the 3rd headline should match the 1st article

    Scenario: Can add a post to the front page
      When I visit "/news/"
      And I click "Add Article"
      And I enter the headline "This is a new article"
      And I add some article content
      And click "Save"
      Then the 1st headline should be "This is a new article"
      And when I visit "/news/" again later
      Then the 1st headline should still be "This is a new article"
