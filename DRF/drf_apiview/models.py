from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField( max_length=50)
    org_id = models.IntegerField(null=True) 

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)