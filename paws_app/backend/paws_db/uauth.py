# USER AUTHENTICATION FUNCTIONS

from django.http import HttpResponse, HttpResponseBadRequest
from .models import UserAuth

class uauthConstants:
    unameTag = 'username'
    pwTag = 'password'
    roleTag = 'role'
    dspTag = 'disp_name'

# Check if a user exists
def userExists (uname):
    try:
        UserAuth.objects.get(uname=uname)

        return True
    except UserAuth.DoesNotExist:
        return False

# Handle login
def userLogin (request):
    try:
        if uauthConstants.unameTag not in request.headers or uauthConstants.pwTag not in request.headers:
            return HttpResponseBadRequest("Failed login: missing parameters")

        uname = request.headers[uauthConstants.unameTag]
        pw = request.headers[uauthConstants.pwTag]

        user = UserAuth.objects.get(uname=uname, pw=pw)

        # Values to return: user role
        response = HttpResponse("Login successful")
        response.headers[uauthConstants.roleTag] = user.role

        return response
    except UserAuth.DoesNotExist:
        return HttpResponseBadRequest("Incorrect username or password")

# Handle user registration
# Precondition: Must have username and password in request header
def regUser (request):
    if uauthConstants.unameTag not in request.headers or uauthConstants.pwTag not in request.headers:
        return HttpResponseBadRequest("Failed user registration: missing parameters")

    uname = request.headers[uauthConstants.unameTag]
    pw = request.headers[uauthConstants.pwTag]
    role = request.headers[uauthConstants.roleTag]
    dspName = request.headers[uauthConstants.dspTag]

    if userExists(uname):
        return HttpResponseBadRequest("Failed user registration: user already exists")

    # Insert user to database
    user = UserAuth(uname=uname, pw=pw, role=role, disp_name=dspName)
    user.save()

    response = HttpResponse("User registration successful")

    return response

# Change a user's password
def changePw (request):
    if uauthConstants.unameTag not in request.headers:
        return HttpResponseBadRequest("Failed user modification: missing parameters")

    # TODO: Check if old pw match?

    uname = request.headers[uauthConstants.unameTag]

    try:
        # Get user
        user = UserAuth.objects.get(uname=uname)

        # Apply changes
        user.save()
    except UserAuth.DoesNotExist:
        return HttpResponseBadRequest("Failed user modification: user does not exist")

# Change a user's role
def changeRole (request):
    pass

# Delete a user from the database