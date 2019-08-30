from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('all/', QuestionsAll.as_view()),
    path('reverse/', QuestionsAllReverse.as_view()),
    path('<int:id>/', QuestionsbyID.as_view() , name='questions'),
    path('<int:id>/hint1', QuestionHint1.as_view() , name='questionHint1'),
    path('<int:id>/hint2', QuestionHint2.as_view() , name='questionHint2'),
    path('<int:id>/hint3', QuestionHint3.as_view() , name='questionHint3'),
    path('<int:id>/hint4', QuestionHint4.as_view() , name='questionHint4'),
    path('<int:id>/hints', QuestionHintAll.as_view() , name='questionHints'),
]