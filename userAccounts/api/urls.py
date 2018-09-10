from django.urls import path, include
from .views import *

urlpatterns = [
    path('retrieve/+<int:username>', Retrieve.as_view()),
    path('update/+<int:username>', Update.as_view()),
    path('create/new', Create.as_view()),
    path('create/otp', OTPVerification.as_view()),
    path('create/otpverified', OTPVerified.as_view()),
    path('create/uploadPic', uploadProfile.as_view()),
    path('forgotPass/', ForgotPassword.as_view()),
    path('forgotPass/otp', ForgotPasswordOTP.as_view()),
    path('forgotPass/otpverified', ForgotPasswordOTPVerified.as_view()),
    path('answer/', Answer.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
    path('leaderboard/', Leaderboard.as_view())
]