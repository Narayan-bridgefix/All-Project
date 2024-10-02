from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(User):
    remember_me = models.BooleanField(default=False,null=True)
    
class Post_Image(models.Model):
    image =  models.ImageField(upload_to='images/') 
    like = models.IntegerField(default=0)
      
class Like_Image(models.Model):
    post_id = models.ForeignKey("Post_Image", on_delete=models.CASCADE)  
    user = models.ForeignKey("User", on_delete=models.CASCADE)  
    
class Comment_Image(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)  
    post_id = models.ForeignKey("Post_Image", on_delete=models.CASCADE)
    comment = models.CharField( max_length=50)
    
class Request_User(models.Model):
    request_by = models.ForeignKey("User",related_name="request_by", on_delete=models.CASCADE)
    request_to = models.ForeignKey("User", related_name="requested_to", on_delete=models.CASCADE)
    request_accepted = models.BooleanField(default=False)