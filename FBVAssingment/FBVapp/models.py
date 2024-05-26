from django.db import models

# Create your models here.
class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    travelPoints = models.DecimalField(max_digits=10,decimal_places=3)


    def __str__(self):
        return self.name 

