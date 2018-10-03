# Kleos2k18 App Server
# Worthless Backend of some crap Android project
##### Deployed at https://kleos2k18.appspot.com
##### Important Note:- Phone Number with country code is username
## It Contains 3 Apps 
* [Questions](https://github.com/Shritesh99/Kleos2k18-server#questions-) 
* [Sponsors](https://github.com/Shritesh99/Kleos2k18-server#sponsors--to-fetch-all-sponsors-as-list) 
* [Users](https://github.com/Shritesh99/Kleos2k18-server#users--user-based-apis)

## Questions:- 
### To Fetch a Question by id:-
#### ID is Question's Level by which you have to fetch
```
https://kleos2k18.appspot.com/questions/api/{id} # Request method - GET
```
###### Response Format:-
```
{
  'title': '<One Line Title>', 
  'question': '<Long Text>', 
  'image': '<Image Url>'
}
```
### To Fetch all Questions:-
```
https://kleos2k18.appspot.com/questions/api/all # Request method - GET
```
###### Response Format:-
```
{
  [
   {
    'title': '<One Line Title>', 
    'question': '<Long Text>', 
    'image': '<Image Url>'
    },
    {
    'title': '<One Line Title>', 
    'question': '<Long Text>', 
    'image': '<Image Url>'
    },
    .
    .
    .
    . All Questions
  ]
}
```
### To Fetch all Questions in Reverse order:-
```
https://kleos2k18.appspot.com/questions/api/reverse # Request method - GET
```
###### Response Format:-
```
{
 [
   {
    'title': '<One Line Title>', 
    'question': '<Long Text>', 
    'image': '<Image Url>'
    },
    {
    'title': '<One Line Title>', 
    'question': '<Long Text>', 
    'image': '<Image Url>'
    },
    .
    .
    .
    . All Questions in reverse
 ]
} 
```
### To Fetch Question's First Hint by ID:-
```
https://kleos2k18.appspot.com/questions/api/{id}/hint1 # Request method - GET
```
###### Response Format:-
```
{
  'title': '<One Line Title>', 
  'hint1': '<One Line Hint>'
}
```
### To Fetch Question's Second Hint by ID:-
```
https://kleos2k18.appspot.com/questions/api/{id}/hint2 # Request method - GET
```
###### Response Format:-
```
{
  'title': '<One Line Title>', 
  'hint2': '<One Line Hint>'
}
```
### To Fetch Question's Third Hint by ID:-
```
https://kleos2k18.appspot.com/questions/api/{id}/hint3 # Request method - GET
```
###### Response Format:-
```
{
  'title': '<One Line Title>', 
  'hint3': '<One Line Hint>'
}
```
### To Fetch Question's Forth Hint by ID:-
```
https://kleos2k18.appspot.com/questions/api/{id}/hint4 # Request method - GET
```
###### Response Format:-
```
{
  'title': '<One Line Title>', 
  'hint4': '<One Line Hint>'
}
```

## Sponsors:- To Fetch All Sponsors as List
```
https://kleos2k18.appspot.com/sponsors/api/list # Request method - GET
```
###### Response Format:-
```
{
[
  {  
     "name":"<Name>",
     "description":"<Short Description>",
     "url":"<Url>",
     "image":"<Image Url>"
 },
 {  
     "name":"<Name2>",
     "description":"<Short Description>",
     "url":"<Url>",
     "image":"<Image Url>"
 }
 .
 .
 .
 .
]
}
```

## Users:- User based APIs
### To Retrieve user's all details any time:-
```
https://kleos2k18.appspot.com/user/api/retrieve/{Phone Number} # Request method - GET, Phone Number must starts with +91xxxxxxxxxx
```
###### Response Format:-
```
{
  'username': '<Phone Number>',
  'email': '<email>',
  'first_name': '<First Name>',
  'last_name': '<Last Name>',
  'college': '<College>',
  'level':'<Level integer>'
  'profile':<Image Url>
}
```

### To Login a User:-
#### Send Phone Number as username and password to server as POST Method
###### Format:-
```
   username:<Phone Number>
   password:<Password>
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/rest-auth/login # Request method - POST
```
###### Response:-
```
   'token':'<Auth Token>'
```
##### Then call Retrieve url to get users's all data

### To Create a User:-
#### User can be created in 3 steps:-
#### 1. Take users Phone Number and send to server as POST Method
##### Send Phone Number as username to server as POST Method
###### Format:-
```
   username:<Phone Number>
   password:<password>
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/create/ # Request method - POST
```
###### Response:-
```
{ 
   "message": "OTP Sent Successfully"
}
```
#### 2. Take users Phone Number, otp and send to server as POST Method
##### Send Phone Number as username and otp to server as POST method
###### Format:-
```
    username:<Phone Number>
    otp:<OTP>
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/create/otp # Request method - POST
```
###### Response:-
```
{ 
   "message": "Otp Verified"
}
```
##### Note:- If OTP verification failed then follow back from step 1

#### 3. If OTP verified then set user's further details
##### Send all details to server as Post method
###### Format:-
```
   username:<Phone Number>
   first_name:<First Name>
   last_name:<Last name>
   email:<email> 
   profile:<Image File>
   college:<college> 
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/create/otpverified # Request method - POST
```
###### Response:-
```
{ 
  "message": "User Created Succesfully"
}
```

### To submit an answer:-
#### Send username, question number, answer to Server as POST method
###### Format:-
```
     username:<Phone Number>
     questionID:<Integer To identify which question>
     answer:<Long Answer>
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/answer/ # Request method - POST
```
###### Response:-
```
{ 
   "message": "Congratulations your answer is correct"
}
```
### To Fetch Current Leaderboard:-
```
https://kleos2k18.appspot.com/user/api/leaderboard/ # Request method - GET
```
###### Response Format:-
```
{
[
  {
  'username': '<Phone Number>',
  'email': '<email>',
  'first_name': '<First Name>',
  'last_name': '<Last Name>',
  'college': '<College>',
  'level':'<Level integer>'
  'profile':<Image Url>
 },
 {
  'username': '<Phone Number>',
  'email': '<email>',
  'first_name': '<First Name>',
  'last_name': '<Last Name>',
  'college': '<College>',
  'level':'<Level integer>'
  'profile':<Image Url>
 },
 .
 .
 .
 .
 . 10 Items
]
}
```

### To Update Current User's Data:-
#### Send data to server as POST method
###### Format:-
```
    first_name:<First Name>
    last_name:<Last name>
    password:<Password>
    email:<email> 
    profile:<Image File>
    college:<college> 
```
#### Note:- you can also send any of the above fileds individually or in combination with others.
###### Response:-
```
{
   "message": "User Updated successfully"
}
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/update/{Phone Number} # Request method - PUT, Phone Number must starts with +91xxxxxxxxxx
```

### If user Forgot's password:-
#### Password be changed in 3 steps:-
#### 1. Take users Phone Number and send to server as PUT Method
##### Send Phone Number as username to server as PUT Method
###### Format:-
```
   username:<Phone Number>
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/fotgotPass/ # Request method - PUT
```
###### Response:-
```
{ 
   "message": "OTP Sent Successfully"
}
```
#### 2. Take users Phone Number, otp and send to server as PUT Method
##### Send Phone Number as username and otp to server as PUT method
###### Format:-
```
 username:<Phone Number>
 otp:<OTP>
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/forgotPass/otp # Request method - PUT
```
###### Response:-
```
{ 
   "message": "Otp Verified"
}
```
##### Note:- If OTP verification failed then follow back from step 1

#### 3. If OTP verified then set user's new password details
##### Send all details to server as Post method
###### Format:-
```
    username:<Phone Number>
    password:<password>
```
###### To:-
```
https://kleos2k18.appspot.com/user/api/forgotPass/otpverified # Request method - PUT
```
###### Response:-
```
{ 
   "message": "password updated successfully"
}
```

      
      
