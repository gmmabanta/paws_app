from tkinter import CASCADE
from turtle import setx
from unicodedata import name
from django.db import models

class Client(models.Model):
    class Meta:
        db_table = 'client'

    frst_name = models.CharField(max_length=80)
    lst_name = models.CharField(max_length=40)
    addr = models.CharField(max_length=200)
    webst = models.CharField(max_length=40)
    fb = models.CharField(max_length=40)
    remarks = models.CharField(max_length=500)

class RescueDetail(models.Model):
    class Meta:
        db_table = 'rescue_detail'

    rescuer = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    addr = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)
    with_legal_case = models.BooleanField()

class FosterDetail(models.Model):
    class Meta:
        db_table = 'foster_detail'

    fosterer = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    rel_date = models.DateField()
    ret_date = models.DateField()

class Animal(models.Model):
    class Meta:
        db_table = 'animal'

    SEX_CHOICES = [
        ('M', 'Male')
       ,('F', 'Female')
    ]

    BREED_SPECIES = [
        #Place list of breeds here as tuples: (<Breed>, <Specie>)
        #e.g. ('Shih Tzu', 'Dog')
        
        ('Aspin', 'Dog')
       ,('Puspin', 'Cat')
    ]

    name = models.CharField(max_length=80)
    adm_date = models.DateField()
    fost_parc = models.CharField(max_length=80)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    breed = models.CharField(max_length=30, choices=BREED_SPECIES)
    desc = models.CharField(max_length=1000)
    hist = models.CharField(max_length=1000)
    rescue_det = models.ForeignKey(RescueDetail, blank=True, null=True, on_delete=models.SET_NULL)
    foster_det = models.ForeignKey(FosterDetail, blank=True, null=True, on_delete=models.SET_NULL)
    init_wt = models.DecimalField(max_digits=5, decimal_places=2)

class ClientContact(models.Model):
    class Meta:
        db_table = 'client_contact'

    CONTACT_CHOICES = [
        ('E', 'Email'),
        ('T', 'Telephone'),
    ]

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=1, choices=CONTACT_CHOICES)
    contact = models.CharField(max_length=40)

# class MedHist(models.Model):
#     anim = models.ForeignKey(Animal.id, on_delete=models.CASCADE)
#     date = models.DateField()
#     wt = models.DecimalField(max_digits=5, decimal_places=2)
#     ## TODO: add details for findings, vaccination, deworming, spay/neuter

class UserAuth(models.Model):
    class Meta:
        db_table = 'user_auth'

    USER_ROLE = [
        ('gst', 'Guest'),
        ('adm', 'Admin'),
        ('vet', 'Veterinarian')
    ]

    uname = models.CharField(primary_key=True, max_length=50, blank=False, null=False)
    pw = models.CharField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=3, choices=USER_ROLE, blank=False, null=False, default='gst')
