# USER AUTHENTICATION FUNCTIONS

from django.http import HttpResponse, HttpResponseBadRequest
from .models import UserAuth

# Check if a user exists
def userExists (uname):
    try:
        user = UserAuth.objects.get(uname=uname)

        return True
    except UserAuth.DoesNotExist:
        return False

# Handle login
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

# Handle user registration
# Precondition: Must have username and password in request header
def regUser (request):
    unameTag = 'username'
    pwTag = 'password'

    if unameTag not in request.headers or pwTag not in request.headers:
        return HttpResponseBadRequest("Failed user registration: missing parameters")

    uname = request.headers[unameTag]
    pw = request.headers[pwTag]

    if userExists(uname):
        return HttpResponseBadRequest("Failed user registration: user already exists")

    # TODO: Insert user to database
    response = HttpResponse("User registration successful")

    return response

# Modify info about a user
def modifyUser (request):
    unameTag = 'username'

    if unameTag not in request.headers:
        return HttpResponseBadRequest("Failed user modification: missing parameters")

    # Need to verify if user requesting for change is admin?

    uname = request.headers[unameTag]

    user = UserAuth.objects.get(uname=uname)

# Delete a user from the database