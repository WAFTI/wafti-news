from news_rhino.models import Article
from rest_framework import serializers


class ArticleSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ()
