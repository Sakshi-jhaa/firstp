from django.db import models

# Create your models here.
class Destination(models.Model):
    # id: int. db will automatically create a primary key
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    prices=models.IntegerField()
    offer=models.BooleanField(default=False)
    cost=models.IntegerField()
