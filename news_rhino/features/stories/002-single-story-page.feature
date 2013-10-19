Feature: Single story page

Scenario: Article title appears as subheading
  Given the site contains an article
  And that article has headline "This is a test article"
  And that article has id 1
  When I visit "/news/1"
  Then I see the headline "This is a test article"
