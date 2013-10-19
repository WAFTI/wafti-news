from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from news_rhino.models import Article
from news_rhino.serialisers import ArticleSerialiser


def index(request):
    context = {}
    return render(request, 'news_rhino/index.html', context)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
