import datetime
from django.db import models
from django.contrib.markup.templatetags import markup
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


class Article(models.Model):
    headline = models.CharField(max_length=300)
    content = models.TextField()
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()

    def html(self):
        return markup.markdown(self.content)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Article, self).save(*args, **kwargs)
