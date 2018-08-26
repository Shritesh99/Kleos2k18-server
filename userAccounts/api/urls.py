from django.urls import path, include
from .views import *

urlpatterns = [
    path('retrieve/+<int:username>', Retrieve.as_view()),
    path('update/+<int:username>', Update.as_view()),
    path('create/', Create.as_view()),
    path('forgotPass/', ForgotPassword.as_view()),
    path('answer/', Answer.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
]