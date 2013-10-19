from lettuce import step, world
from news_rhino.models import Article

@step(u'Given the site contains an article')
def given_the_site_contains_an_article(step):
    world.article = Article()


@step(u'And that article has headline "([^"]*)"')
def set_article_headline(step, headline):
    world.article.headline = headline


@step(u'And that article has id (\d+)')
def set_article_pk(step, pk):
    world.article.pk = pk

