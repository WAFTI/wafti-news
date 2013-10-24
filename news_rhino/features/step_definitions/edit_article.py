from lettuce import step, world
import time


@step(u'And click the edit button')
def click_button(step):
    time.sleep(60)
    css = "a.create-ui-btn"
    xpath = '//a[@class="create-ui-btn" and not(@disabled) and not(contains(@style,\'display:none\'))]'
    world.browser.is_element_present_by_xpath(xpath, wait_time=60)
    print world.browser.html
    world.browser.find_by_xpath(xpath).first.click()
