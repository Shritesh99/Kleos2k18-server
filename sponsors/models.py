from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from Kleos2k18 import settings


def get_upload_url(instance , filename):
        return 'media/sponsors/%s' % (filename)


class Sponsor(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    description = models.TextField(max_length=100)
    url = models.URLField(name='url',max_length=200)
    image = models.ImageField(upload_to = get_upload_url, blank = True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural='Sponsors'
