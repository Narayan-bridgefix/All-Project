from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasklist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    task=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.task
    
class User(User):
    # otp=models.CharField(max_length=6,null=True)
    remember_me = models.BooleanField(default=False,null=True)
    
# class RegistrationOtp(User):
#     otp1=models.CharField(max_length=10)    