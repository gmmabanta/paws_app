from django.http import HttpResponse, HttpResponseBadRequest
from .models import UserAuth

def userLogin (request):
    try:
        unameTag = 'username'
        pwTag = 'password'

        if unameTag not in request.headers or pwTag not in request.headers:
            return HttpResponseBadRequest("Failed login: missing parameters")

        uname = request.headers[unameTag]
        pw = request.headers[pwTag]

        UserAuth.objects.get(uname=uname, pw=pw)
        # TODO: return user?
        return HttpResponse("Login successful") #add info for session here??
    except UserAuth.DoesNotExist:
        return HttpResponseBadRequest("Incorrect username or password")
