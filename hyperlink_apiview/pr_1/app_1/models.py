from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    
class ref(models.Model):
    ref_name = models.ForeignKey("Student",  on_delete=models.CASCADE)
    
    
    

class Author(models.Model):
    AuthorName = models.CharField(max_length=255, unique=False)

class Book(models.Model):
    BookName = models.CharField(max_length=255)
    Author = models.ForeignKey('Author',on_delete=models.CASCADE)



class ModelA(models.Model):
   pass
 
class ModelB(models.Model):
   a = models.ForeignKey(ModelA, on_delete=models.CASCADE)
   
   
   
   
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
    
class pro(Track):
    class Meta:
        proxy = True
    def __str__(self):
        return self.duration