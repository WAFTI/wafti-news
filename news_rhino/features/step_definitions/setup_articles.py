import random
from lettuce import step, world
from news_rhino.models import Article
from loremipsum import get_paragraphs


def create_article(article_id):
    article = Article()
    article.headline = 'This is a basic article %s' % article_id

    world.content = "\n\n".join(get_paragraphs(random.randint(1, 6)))
    article.content = world.content

    article.pk = article_id
    article.save()
    world.articles[article_id] = article


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


@step(u'And that article has (\d+) paragraph\(s\) of content')
def generate_content(step, paragraph_count):
    world.content = "\n\n".join(get_paragraphs(int(paragraph_count)))
    world.article.content = world.content


@step(u'Given the site contains a basic article')
def given_the_site_contains_a_basic_article(step):
    world.article = Article()
    world.article.headline = "This is a basic article"

    world.content = "\n\n".join(get_paragraphs(5))
    world.article.content = world.content

    world.article.pk = 1
    world.article.save()


@step(u'Given the site contains 3 basic articles added in date order')
def given_the_site_contains_3_basic_articles_added_in_date_order(step):
    create_article(1)
    create_article(2)
    create_article(3)