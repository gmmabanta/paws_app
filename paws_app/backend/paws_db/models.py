from turtle import setx
from unicodedata import name
from django.db import models

class Client(models.Model):
    frst_name = models.CharField(max_length=80)
    lst_name = models.CharField(max_length=40)
    addr = models.CharField(max_length=200)
    webst = models.CharField(max_length=40)
    fb = models.CharField(max_length=40)
    remarks = models.CharField(max_length=500)

class ShelterAnimal(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    BREED_SPECIES = [
        """
        Place list of breeds here as tuples: (<Breed>, <Specie>)
        e.g. ('Shih Tzu', 'Dog')
        """
    ]

    name = models.CharField(max_length=80)
    adm_date = models.DateField()
    fost_parc = models.CharField(max_length=80)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    breed = models.CharField(choices=BREED_SPECIES)
    desc = models.CharField(max_length=1000)
    hist = models.CharField(max_length=1000)
    rescuer = models.ForeignKey(Client.id, blank=True, null=True)
    foster = models.ForeignKey(Client.id, blank=True, null=True)
    init_wt = models.DecimalField(max_digits=5, decimal_places=2)

class ClientContact(models.Model):
    CONTACT_CHOICES = [
        ('E', 'Email'),
        ('T', 'Telephone'),
    ]

    client_id = models.ForeignKey(Client.id)
    contact_type = models.CharField(max_length=1, choices=CONTACT_CHOICES)
    contact = models.CharField(max_length=40)

class UserAuth(models.Model):
    uname = models.CharField(primary_key=True)
    pw = models.CharField()
