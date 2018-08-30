import json
from random import randint
from django.contrib.auth.hashers import make_password
import requests
from django.http import HttpResponse
from rest_framework import generics

from Kleos2k18 import settings
from userAccounts.api.serializers import UserSerializer
from userAccounts.models import User
from questions.models import Question


class Retrieve(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        username = '+%s' % (kwargs['username'])
        base_url = settings.MEDIA_URL

        qs = User.objects.values('username', 'first_name', 'last_name', 'email', 'profile', 'college', 'level')
        qs = qs.filter(username=username)
        if qs.count() != 0:
            base_url = settings.MEDIA_URL
            data = {
                'username': qs.values('username')[0]['username'],
                'email': qs.values('email')[0]['email'],
                'first_name': qs.values('first_name')[0]['first_name'],
                'last_name': qs.values('last_name')[0]['last_name'],
                'college': qs.values('college')[0]['college'],
                'level': qs.values('level')[0]['level'],
                'profile': base_url + str(qs.values('profile')[0]['profile'])
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                "message": "Invalid User"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class Create(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', "")
        password = make_password(request.POST.get('password', ""))
        otp = randint(100000, 999999)
        authKey = '232164AmNrF6I3wJ5b7d7e89'
        url = 'http://control.msg91.com/api/sendotp.php?authkey=' + authKey
        url += '&message=Welcome to Kleos Your Verification code is ' + str(otp)
        url += '&sender=KLEOSAPP'
        url += '&mobile=' + username
        url += '&otp=' + str(otp)
        print(requests.request('POST', url))
        user = User.objects.update_or_create(
            username=username,
            password=password,
            otp=otp,
        )
        data = {"message": "OTP Sent Successfully"}
        return HttpResponse(json.dumps(data), content_type='application/json')


class OTPVerification(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', "")
        otp = request.POST.get('otp', "")
        data = {}
        if otp == User.objects.values('otp').filter(username=username):
            data = {
                "message": "Otp Verified"
            }
        else:
            qs = User.objects.filter(username=username).delete()
            data = {
                "message": "OTP didn't match"
            }
        return HttpResponse(json.dumps(data), content_type='application/json')


class OTPVerified(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', "")
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        email = request.POST.get('email', "")
        profile = request.FILES.get('profile', None)
        college = request.POST.get('college', "")
        otp = request.POST.get('otp', "")
        data = {}
        user = User.objects.filter(username=username).update(email=email, first_name=first_name, last_name=last_name,
                                                             profile=profile, college=college)
        data = {
            "message": "User Created Succesfully"
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


class Update(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        username = '+%s' % (kwargs['username'])
        if User.objects.filter(username=username).exists():

            first_name = request.PUT.get('first_name', User.objects.values('first_name').filter(username=username))
            last_name = request.PUT.get('last_name', User.objects.values('last_name').filter(username=username))
            password = make_password(
                request.PUT.get('password', User.objects.values('password').filter(username=username)))
            email = request.PUT.get('email', User.objects.values('email').filter(username=username))
            profile = request.FILES.get('profile', User.objects.values('profile').filter(username=username))
            college = request.PUT.get('college', User.objects.values('college').filter(username=username))
            user = User.objects.filter(username=username).update(first_name=first_name, last_name=last_name,
                                                                 password=password, email=email, profile=profile,
                                                                 college=college)
            return HttpResponse(json.dumps({"message": "User Updated successfully"}), content_type='application/json')

        else:
            return HttpResponse(json.dumps({"message": "User does not exist"}), content_type='application/json')


class ForgotPassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        username = request.data['username']
        otp = request.PUT.get('otp', "")
        password = make_password(request.PUT.get('password', ""))
        if username != "" and otp == "":
            user = User.objects.filter(username=username)
            if user.exists():
                otp = randint(100000, 999999)
                authKey = '232164AmNrF6I3wJ5b7d7e89'
                url = 'http://control.msg91.com/api/sendotp.php?authkey=' + authKey
                url += '&message=Welcome to Kleos Your Verification code is ' + str(otp)
                url += '&sender=KLEOSAPP'
                url += '&mobile=' + username
                url += '&otp=' + str(otp)
                print(requests.request('POST', url))
                user.update(otp=otp)
                data = {"message": "OTP Sent Successfully"}
            else:
                data = {"message": "User does not exist"}
            return HttpResponse(json.dumps(data), content_type='application/json')


class ForgotPasswordOTP(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        username = request.data['username']
        otp = request.PUT.get('otp', "")
        data = {}
        if otp == User.objects.values('otp').filter(username=username):
            data = {"message": "Otp verified"}
        else:
            data = {"message": "otp didn't match"}

        return HttpResponse(json.dumps(data), content_type='application/json')


class ForgotPasswordOTPVerified(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        username = request.data['username']
        password = make_password(request.PUT.get('password', ""))
        user = User.objects.filter(username=username).update(password=password)
        data = {"message": "password updated successfully"}
        return HttpResponse(json.dumps(data), content_type='application/json')


class Answer(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', "")
        questionID = request.POST.get('questionID', "")
        answer = request.POST.get('answer', "")

        if username != "" and questionID != "" and answer != "":
            if str(answer).lower().replace(" ", "") == str(
                    Question.objects.values('answer').filter(questionID=questionID)).lower().replace(" ", ""):
                user = User.objects.filter(username=username).update(level=questionID)
                data = {
                    "message": "Congratulations your answer is correct"
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {
                    "message": "Sorry wrong answer"
                }
                return HttpResponse(json.dumps(data), content_type='application/json')

        else:
            data = {
                "message": "bad request"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class Leaderboard(generics.ListAPIView):
    queryset = User.objects.all().order_by('-level')[:10]
    serializer_class = UserSerializer
