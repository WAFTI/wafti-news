from lettuce import step, world
from lxml import html


@step(r'I visit "(.*)"')
def access_url(step, url):
    response = world.browser.get(url, Accept='text/html')
    world.dom = html.fromstring(response.content)
