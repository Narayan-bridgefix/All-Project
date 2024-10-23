from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    
class ref(models.Model):
    ref_name = models.ForeignKey("Student",  on_delete=models.CASCADE)
    
    
    

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
