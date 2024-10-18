from django.db import models

# Create your models here.
class Postgres_data(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=10)
    
class Postgres_employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=10)
    
class newmodel(models.Model):
    name = models.CharField( max_length=50)
    