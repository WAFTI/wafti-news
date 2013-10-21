from django.db import models
from django.contrib.markup.templatetags import markup


class Article(models.Model):
    headline = models.CharField(max_length=300)
    content = models.TextField()

    def html(self):
        return markup.markdown(self.content)
