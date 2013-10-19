from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=300)
