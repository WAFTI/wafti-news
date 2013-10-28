from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from news_rhino.models import Article
from news_rhino.serialisers import ArticleSerialiser
from rest_framework.response import Response


def index(request):
    context = {}
    return render(request, 'news_rhino/index.html', context)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser

    def retrieve(self, request, *args, **kwargs):

        response = super(ArticleViewSet, self).retrieve(
            request, *args, **kwargs)

        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data},
                            template_name='news_rhino/article_detail.html')
        return response

    def update(self, request, *args, **kwargs):
        return super(ArticleViewSet, self).update(
            request, *args, **kwargs)
