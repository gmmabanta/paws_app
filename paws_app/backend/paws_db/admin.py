from django.contrib import admin

# Register your models here.

from .models import Client, RescueDetail, FosterDetail, Animal, ClientContact, UserAuth

admin.site.register(Client)
admin.site.register(RescueDetail)
admin.site.register(FosterDetail)
admin.site.register(Animal)
admin.site.register(ClientContact)
admin.site.register(UserAuth)