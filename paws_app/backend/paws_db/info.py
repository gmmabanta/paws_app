# INFORMATION PAGE FUNCTIONS

from django.http import HttpResponse, HttpResponseBadRequest
from .models import UserAuth

# Check if an animal exists
def userExists (id):
    try:
        animal = Animal.objects.get(id=id)

        return True
    except Animal.DoesNotExist:
        return False

# Insert new information (about an animal)
def addInfo (request):
    animalTag = 'animalID'

    if animalTag not in request.headers:
        return HttpResponseBadRequest("Information addition failed: missing parameters")

    animalId = request.headers[animalTag]

    if animalExists(animalId):
        return HttpResponseBadRequest("Information addition failed: animal already exists")

    # TODO: Insert animal and return response
    response = HttpResponse("Information deletion successful")

    return response

# Modify information
def modifyInfo (request):
    animalTag = 'animalID'

    if animalTag not in request.headers:
        return HttpResponseBadRequest("Information modification failed: missing parameters")

    animalId = request.headers[animalTag]

    if not animalExists(animalId):
        return HttpResponseBadRequest("Information modification failed: animal does not exist")

    # TODO: Modify animal and return response
    response = HttpResponse("Information modification successful")

    return response

# Delete information
def deleteInfo (request):
    animalTag = 'animalID'

    if animalTag not in request.headers:
        return HttpResponseBadRequest("Information deletion failed: missing parameters")

    animalId = request.headers[animalTag]

    if not animalExists(animalId):
        return HttpResponseBadRequest("Information deletion failed: animal does not exist")

    # TODO: Delete animal and return response
    response = HttpResponse("Information deletion successful")

    return response

# Retrieve information to display
def getInfo (request):
    animalTag = 'animalID'

    if animalTag not in request.headers:
        return HttpResponseBadRequest("Information retrieval failed: missing parameters")

    animalId = request.headers[animalTag]

    if not animalExists(animalId):
        return HttpResponseBadRequest("Information retrieval failed: animal does not exist")

    # TODO: Get animal and return info in response
    response = HttpResponse("Information retrieval successful")

    return response
