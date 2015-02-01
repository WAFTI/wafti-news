import random
from lettuce import step, world
import time
from loremipsum import get_paragraphs


@step(u'And click the edit button')
def click_button(step):
    css = "a.create-ui-btn"
    #xpath = '//a[@class="create-ui-btn" and not(@disabled) and not(contains(@style,\'display:none\'))]'
    xpath = '//*[@id="midgardcreate-edit"]/a'
    world.browser.is_element_present_by_xpath(xpath, wait_time=10)
    world.browser.find_by_xpath(xpath).first.click()


@step(u'And change the headline to "([^"]*)"')
def change_headline(step, new_headline):
    headline = world.browser.find_by_css('h2').first
    headline.click()
    headline.fill(new_headline)

@step(u'And I enter the headline "([^"]*)"')
def and_i_enter_the_headline_group1(step, new_headline):
    headline = world.browser.find_by_css('h2.inPlaceholderMode').first
    headline.click()
    headline.fill(new_headline)

@step(u'And click "Save"')
def click_save(step):
    world.browser.find_by_css('li#midgardcreate-save a').first.click()


@step(u'And I click "([^"]*)"')
def and_i_click_group1(step, group1):
    world.browser.find_by_css('.midgard-create-add').first.click()


@step(u'And I add some article content')
def and_i_add_some_article_content(step):
    world.content = '<p>%s</p>' % '</p><p>'.join(get_paragraphs(random.randint(1, 6)))
    body = world.browser.find_by_css('div.inPlaceholderMode').first
    body.click()
    body.fill(world.content)
