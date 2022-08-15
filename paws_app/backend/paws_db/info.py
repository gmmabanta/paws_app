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

# Modify information

# Delete information

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
