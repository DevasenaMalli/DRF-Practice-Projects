from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10) 
    operatingAirline = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20,blank=True,null=True)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middletName = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    


class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)    
    

@receiver(post_save,sender=settings.AUTH_USER_MODEL) 
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
