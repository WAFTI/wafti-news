import sys
from lettuce import step, world
from hamcrest import *
from django.contrib.markup.templatetags import markup
from lxml import html
from formencode.doctest_xml_compare import xml_compare


@step(u'Then I see the header "([^"]*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')[0]
    assert_that(header.text, is_(text))


@step(u'Then I see the headline "([^"]*)"')
def see_headline(step, text):
    header = world.dom.cssselect('h2')[0]
    assert_that(header.text, is_(text))


@step(u'Then I see the content')
def then_i_see_the_content(step):
    expected = html.fromstring(
        "<div>%s</div>" % markup.markdown(world.content))
    actual = world.dom.cssselect('article div')[0]

    reporter = lambda x: sys.stdout.write(x + "\n")
    assert xml_compare(expected, actual, reporter)
