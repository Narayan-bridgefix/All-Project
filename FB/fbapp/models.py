from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(User):
    remember_me = models.BooleanField(default=False,null=True)
    
class UserData(models.Model):
    post = models.FileField(upload_to = "images")
    like = models.IntegerField(default=0)
    Comment = models.CharField(max_length=50,null=True)
