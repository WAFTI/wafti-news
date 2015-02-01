from news_rhino.models import Article
from rest_framework import serializers
import html2text


class ArticleSerialiser(serializers.HyperlinkedModelSerializer):

    article_id = serializers.Field(source='pk')
    html = serializers.Field(source='html')

    class Meta:
        model = Article
        fields = ('article_id', 'headline', 'content', 'html', 'url')


    def restore_fields(self, data, files):
        if '<http://schema.org/headline>' in data:
            data['headline'] = data['<http://schema.org/headline>']

        if '<http://schema.org/text>' in data:
            data['content'] = data['<http://schema.org/text>']

        data['content'] = html2text.html2text(data['content'])

        return super(ArticleSerialiser, self).restore_fields(data, files)
