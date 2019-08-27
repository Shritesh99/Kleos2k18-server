from ..models import *
from rest_framework import serializers


class SponsorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'description', 'url', 'image')
