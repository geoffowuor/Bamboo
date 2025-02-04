from django.db import models

# Create your models here.
class booking(models.Model):
    name = models.CharField(max_length=50, null=True)  
    contact = models.CharField(max_length=420, null=True)
    email = models.EmailField(null=True)
    arrival = models.DateField(null=True)
    depature = models.DateField(null=True)
    booking_date = models.DateTimeField(auto_now_add=True, null=True)  # Date of application
   
    def __str__(self):
        return self.name
    
    
class reserve(models.Model):
    r_name = models.CharField(max_length=50, null=True)  
    r_contact = models.CharField(max_length=420, null=True)
    when = models.DateField(null=True)
    number = models.IntegerField(null=True)
    reserve_date = models.DateTimeField(auto_now_add=True, null=True)  # Date of application
   
    def __str__(self):
        return self.r_name