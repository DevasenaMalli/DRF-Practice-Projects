from django.db import models, migrations

# Create your models here.




class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName  = models.CharField(max_length=20)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.firstName

class Order(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, default=None,related_name='orders',on_delete=models.CASCADE)
    