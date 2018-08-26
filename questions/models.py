from __future__ import unicode_literals
from django.db import models

# Create your models here.
from Kleos2k18 import settings


def get_upload_url(instance , filename):
    return 'media/Questions/%s'%(filename)

class Question(models.Model):
    title = models.CharField(max_length = 100, unique=True)
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=100)
    image = models.ImageField(upload_to = get_upload_url,blank = True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural='Questions'
