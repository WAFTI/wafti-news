from lettuce import step, world
from news_rhino.models import Article
from loremipsum import get_paragraphs


@step(u'Given the site contains an article')
def given_the_site_contains_an_article(step):
    world.article = Article()


@step(u'And that article has headline "([^"]*)"')
def set_article_headline(step, headline):
    world.article.headline = headline


@step(u'And that article has id (\d+)')
def set_article_pk(step, pk):
    world.article.pk = pk
    world.article.save()


@step(u'And that article has (\d+) paragraph of content')
def generate_content(step, paragraph_count):
    world.content = "\n\n".join(get_paragraphs(int(paragraph_count)))
    world.article.content = world.content
