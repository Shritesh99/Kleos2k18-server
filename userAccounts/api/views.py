import json
from random import randint
from django.contrib.auth.hashers import make_password
import requests
from django.http import HttpResponse
from rest_framework import generics

from userAccounts.api.serializers import UserSerializer
from userAccounts.models import User
from questions.models import Question


class Retrieve(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        username = '+%s' % (kwargs['username'])
        qs = User.objects.values('username', 'first_name', 'last_name', 'email', 'profile', 'college','rank', 'level')
        qs = qs.filter(username=username)
        if qs.count() != 0:
            return HttpResponse(qs, content_type='application/json')
        else:
            data = {
                "message": "Invalid User"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class Create(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST.get('username', "")
            first_name = request.POST.get('first_name', "")
            last_name = request.POST.get('last_name', "")
            password = make_password(request.POST.get('password',""))
            email = request.POST.get('email', "")
            profile = request.FILES.get('profile', None)
            college = request.POST.get('college', "")
            otp = request.POST.get('otp', "")
            if username != "" and otp == "":
                otp = randint(100000, 999999)
                authKey = '232164AmNrF6I3wJ5b7d7e89'
                url = 'http://control.msg91.com/api/sendotp.php?authkey=' + authKey
                url += '&message=Welcome to Kleos Your Verification code is ' + str(otp)
                url += '&sender=KLEOSAPP'
                url += '&mobile=' + username
                url += '&otp=' + str(otp)
                print(requests.request('POST', url))
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    otp=otp,
                )
                data = {"message": "OTP Sent Successfully"}
                return HttpResponse(json.dumps(data), content_type='application/json')
            elif otp != "" and username != "":
                data = {}
                if otp == User.objects.values('otp').filter(username=username):
                    user = User.objects.filter(username=username).update(first_name=first_name, last_name=last_name,
                                                                         profile=profile, college=college)
                    data = {
                        "message": "User Created Succesfully"
                    }
                else:
                    qs = User.objects.filter(username=username).delete()
                    data = {
                        "message": "OTP didn't match"
                    }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {"message": "Bad Request"}
                return HttpResponse(json.dumps(data), content_type='application/json')

        except KeyError:
            print("Key error")
            data = {"message": "Check Missing Keys"}
            return HttpResponse(json.dumps(data), content_type='application/json')


class Update(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        username = '+%s' % (kwargs['username'])
        first_name = request.PUT.get('first_name', User.objects.values('first_name').filter(username=username))
        last_name = request.PUT.get('last_name', User.objects.values('last_name').filter(username=username))
        password = make_password(request.PUT.get('password', User.objects.values('password').filter(username=username)))
        email = request.PUT.get('email', User.objects.values('email').filter(username=username))
        profile = request.FILES.get('profile', User.objects.values('profile').filter(username=username))
        college = request.PUT.get('college', User.objects.values('college').filter(username=username))
        user = User.objects.filter(username=username).update(first_name=first_name, last_name=last_name, password=password, email=email, profile=profile, college=college)
        return HttpResponse(json.dumps({"message": "User Updated successfully"}), content_type='application/json')

class ForgotPassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def put(self, request, *args, **kwargs):
        username = request.data['username']
        otp = request.PUT.get('otp', "")
        password = make_password(request.PUT.get('password', ""))
        if username != "" and otp == "" :
            otp = randint(100000, 999999)
            authKey = '232164AmNrF6I3wJ5b7d7e89'
            url = 'http://control.msg91.com/api/sendotp.php?authkey=' + authKey
            url += '&message=Welcome to Kleos Your Verification code is ' + str(otp)
            url += '&sender=KLEOSAPP'
            url += '&mobile=' + username
            url += '&otp=' + str(otp)
            print(requests.request('POST', url))
            user = User.objects.filter(username=username).update(otp=otp)
            data = {"message": "OTP Sent Successfully"}
            return HttpResponse(json.dumps(data), content_type='application/json')
        elif otp != "":
            data = {}
            if otp == User.objects.values('otp').filter(username=username):
                data = {
                    "message": "otp verified"
                }
            else:
                data = {
                    "message": "otp didn't match"
                }
            return HttpResponse(json.dumps(data), content_type='application/json')
        elif request.PUT.get('password', "") != "":
            user = User.objects.filter(username=username).update(password=password)
            data = {
                "message": "password updated successfully"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {"message": "Bad Request"}
            return HttpResponse(json.dumps(data), content_type='application/json')


class Answer(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', "")
        questionID = request.POST.get('questionID', "")
        answer = request.POST.get('answer', "")

        if username != "" and questionID != "" and answer != "":
            if str(answer).lower().replace(" ", "") == str(Question.objects.values('answer').filter(id=questionID)).lower().replace(" ", ""):
                user = User.objects.filter(username=username).update(level=questionID)
                data = {
                    "level": User.objects.values('level').filter(username=username),
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
