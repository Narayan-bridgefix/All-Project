from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# class TemporaryModel(models.Model):
#     use_in_migrations = False
    
    
# class TemporaryModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     class Meta:
#         managed = False
# class TemporaryModel2(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     class Meta:
#         managed = False
# class TemporaryModel1(models.Manager):
#     use_in_migrations = False
    # name = models.CharField( max_length=50,default="asdf")
    # # ...
    # class Meta:
    #     use_in_migrations = False


# class Publisher(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# class MyManager(models.Manager):
#     use_in_migrations = True


class MyModel(models.Model):
    nme =  models.CharField(max_length=10)
    name =  models.CharField(max_length=10)
    
    # objects = MyManager()
     
     
# class MyManager1(models.Manager):
#     use_in_migrations = False

