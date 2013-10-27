from lettuce import step, world
import time


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


@step(u'And click "Save"')
def click_save(step):
    world.browser.find_by_css('li#midgardcreate-save a').first.click()
