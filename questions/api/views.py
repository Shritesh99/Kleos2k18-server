import json

from django.http import HttpResponse
from rest_framework import generics

from Kleos2k18 import settings
from .serializers import QuestionSerializer
from questions.models import Question


class QuestionsAll(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionsAllReverse(generics.ListAPIView):
    queryset = Question.objects.all().order_by('-questionID')
    serializer_class = QuestionSerializer


class QuestionsbyID(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title', 'question', 'image').filter(questionID=kwargs['id'])
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


class QuestionsReverse(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title', 'question', 'image').filter(questionID=kwargs['id'])
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


class QuestionHint1(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title', 'hint1').filter(questionID=kwargs['id'])
        if qs.count() != 0:
            return HttpResponse(json.dumps(list(qs)[0]), content_type='application/json')
        else:
            data = {
                "message": "Invalid request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class QuestionHint2(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title', 'hint2').filter(questionID=kwargs['id'])
        if qs.count() != 0:
            return HttpResponse(json.dumps(list(qs)[0]), content_type='application/json')
        else:
            data = {
                "message": "Invalid request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class QuestionHint3(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title', 'hint3').filter(questionID=kwargs['id'])
        if qs.count() != 0:
            return HttpResponse(json.dumps(list(qs)[0]), content_type='application/json')
        else:
            data = {
                "message": "Invalid request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class QuestionHint4(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title', 'hint4').filter(questionID=kwargs['id'])
        if qs.count() != 0:
            return HttpResponse(json.dumps(list(qs)[0]), content_type='application/json')
        else:
            data = {
                "message": "Invalid request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')

class QuestionHintAll(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        qs = Question.objects.values('title', 'hint1','hint2','hint3','hint4').filter(questionID=kwargs['id'])
        if qs.count() != 0:
            return HttpResponse(json.dumps(list(qs)[0]), content_type='application/json')
        else:
            data = {
                "message": "Invalid request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')