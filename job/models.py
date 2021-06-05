from django.db import models

# Create your models here.

class Application(models.Model):
    # id: int. db will automatically create a primary key
    job_role=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)
    Specification=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    salary=models.IntegerField()
    apply_date=models.DateField()