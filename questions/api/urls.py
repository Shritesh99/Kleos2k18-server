from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('<int:id>/', QuestionsAll.as_view() , name='questions')
]