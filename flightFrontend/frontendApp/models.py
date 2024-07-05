from django.db import models



class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirline = models.CharField(max_length=50)
    departureCity = models.CharField(max_length=50)
    arrivalCity = models.CharField(max_length=50)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

