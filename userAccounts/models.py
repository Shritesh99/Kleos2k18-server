from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

def get_upload_url(instance, filename):
    return 'media/profile/%s/%s'%(instance.username , filename)


class User(AbstractUser):
    AbstractUser.username = PhoneNumberField(unique=True)
    profile = models.ImageField(upload_to=get_upload_url)
    college = models.CharField(max_length=255, blank=True)
    otp = models.IntegerField(blank=True,null=True)
    level = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name_plural='Users'
