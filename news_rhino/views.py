from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from news_rhino.models import Article
from news_rhino.serialisers import ArticleSerialiser
from rest_framework.response import Response


def index(request):
    return redirect('/news/')


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.order_by('-created')
    serializer_class = ArticleSerialiser

    def list(self, request, *args, **kwargs):
        response = super(ArticleViewSet, self).list(
            request, *args, **kwargs)

        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data},
                            template_name='news_rhino/article_list.html')

        return response

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
