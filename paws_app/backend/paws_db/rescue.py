# RESCUE PAGE FUNCTIONS

from django.http import HttpResponse, HttpResponseBadRequest
from .models import RescueDetail

class rescueConstants:
    idTag = 'id'
    rescuerTag = 'rescuer'
    addrTag = 'address'
    remarkTag =  'remarks'
    legalTag = 'with_legal_case'

# Check if rescuer exists
def rescuerExists (id):
    try:
        RescueDetail.objects.get(id = id)

        return True
    except RescueDetail.DoesNotExist:
        return False

# Insert rescue info
def addRescInfo (request):
    if rescueConstants.rescuerTag not in request.headers or rescueConstants.addrTag not in request.headers or rescueConstants.remarkTag not in request.headers or rescueConstants.legalTag not in request.headers:
        return HttpResponseBadRequest("Failed rescue addition: missing parameters")

# Modify rescue info
def modifyRescInfo (request):
    try:
        if rescueConstants.idTag not in request.headers:
            return HttpResponseBadRequest("Failed rescue modification: missing parameters")

        if rescueConstants.rescuerTag not in request.headers or rescueConstants.addrTag not in request.headers or rescueConstants.remarkTag not in request.headers or rescueConstants.legalTag not in request.headers:
            return HttpResponseBadRequest("Failed rescue modification: missing parameters")

        # Get rescue info
        id = request[rescueConstants.idTag]
        rescue = RescueDetail.objects.get(id = id)
        
        rescuer = request[rescueConstants.rescuerTag]

        if rescue.rescuer != rescuer and not rescuerExists(id = id):
            return HttpResponseBadRequest("Rescuer does not exist")

        # Apply changes
        rescue.rescuer = rescuer
        rescue.addr = request[rescueConstants.addrTag]
        rescue.remarks = request[rescueConstants.remarkTag]
        rescue.with_legal_case = request[rescueConstants.legalTag]

        # Save changes to DB
        rescue.save()
    except RescueDetail.DoesNotExist:
        return HttpResponseBadRequest("Rescue does not exist")


# Delete rescue info
def deleteRescInfo (request):
    pass

# Get rescue info for an animal
def getRescInfo (request):
    pass