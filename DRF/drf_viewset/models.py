from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField( max_length=50)
    org_id = models.IntegerField(null=True)
    
    
class TestS(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(null=True)
    
    
    
class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField()
    
    
    
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
    
    
from time import timezone
class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField( editable=False)
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()