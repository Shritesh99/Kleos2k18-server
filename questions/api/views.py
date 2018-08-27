import json

from django.http import HttpResponse
from rest_framework import generics

from Kleos2k18 import settings
from .serializers import QuestionSerializer
from questions.models import Question


class QuestionsAll(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title','question','image').filter(questionID=kwargs['id'])
        if qs.count() != 0:
            base_url = settings.MEDIA_URL
            data = {
                'title': qs.values('title')[0]['title'],
                'question': qs.values('question')[0]['question'],
                'image': base_url + str(qs.values('image')[0]['image'])
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                "message": "Invalid request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
