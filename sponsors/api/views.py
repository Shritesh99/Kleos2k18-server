from rest_framework import generics
from .serializers import *
from ..models import *

class Sponsors(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializers