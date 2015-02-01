Feature: Ability to edit single article

Scenario: Changing an article's title
  Given the site contains a basic article
  When I visit that article
  And click the edit button
  And change the headline to "This is a different title"
  And click "Save"
  Then the headline should be "This is a different title"
  When I visit that article again later
  Then the headline should still be "This is a different title"
