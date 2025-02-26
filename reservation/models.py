from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False) 
    inventory = models.IntegerField(null=False) 

    def __str__(self): 
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255) 
    no_of_guests = models.IntegerField(null=False) 
    booking_date = models.DateTimeField()

    def __str__(self): 
        return self.name