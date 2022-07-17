from django.http import HttpResponse, HttpResponseBadRequest
from .models import UserAuth

def userLogin (request):
    try:
        unameTag = 'username'
        pwTag = 'password'
        roleTag = 'role'

        if unameTag not in request.headers or pwTag not in request.headers:
            return HttpResponseBadRequest("Failed login: missing parameters")

        uname = request.headers[unameTag]
        pw = request.headers[pwTag]

        user = UserAuth.objects.get(uname=uname, pw=pw)

        # Values to return: user role
        response = HttpResponse("Login successful")
        response.headers[roleTag] = user.role

        return response
    except UserAuth.DoesNotExist:
        return HttpResponseBadRequest("Incorrect username or password")
