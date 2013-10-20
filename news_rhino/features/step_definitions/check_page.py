from lettuce import step, world
from hamcrest import *


@step(u'Then I see the header "([^"]*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')[0]
    assert_that(header.text, is_(text))

@step(u'Then I see the headline "([^"]*)"')
def see_headline(step, text):
    header = world.dom.cssselect('h2')[0]
    assert_that(header.text, is_(text))
