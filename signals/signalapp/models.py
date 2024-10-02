from django.db import models

class User(models.Model):
   # Adding the name
   name = models.CharField(max_length=100)
   # Adding the email
   email = models.EmailField()

   def __str__(self):
      return self.name