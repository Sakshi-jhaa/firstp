from django.db import models

# Create your models here.
class Donation(models.Model):
    # id: int. db will automatically create a primary key
    Donor_name=models.CharField(max_length=100)
    Number_of_items=models.IntegerField()
    Items=models.CharField(max_length=100)
    donation_date=models.DateField()
    cash=models.IntegerField()
    
    
    
    