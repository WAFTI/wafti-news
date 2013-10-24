from lettuce import step, world
from lxml import html


@step(r'I visit "(.*)"')
def access_url(step, url):
    response = world.browser.visit('http://127.0.0.1:8000' + url)

@step(u'When I visit that article')
def when_i_visit_that_article(step):
        response = world.browser.visit('http://127.0.0.1:8000/news/' + str(world.article.pk) + '/')
