from news_rhino.models import Article
from rest_framework import serializers


class ArticleSerialiser(serializers.HyperlinkedModelSerializer):

    html = serializers.Field(source='html')

    class Meta:
        model = Article
        fields = ('headline', 'html')
