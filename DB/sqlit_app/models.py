from django.db import models

# Create your models here.
class Data_sqlite(models.Model):
    name = models.CharField( max_length=50)