import json

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import QuestionSerializer
from questions.models import Question


class QuestionsAll(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get(self, request, *args, **kwargs):
        qs = Question.objects.filter(id=kwargs['id'])
        if qs.count() != 0:
            return HttpResponse(qs, content_type='application/json')
        else:
            data = {
                "message": "Invalid request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
