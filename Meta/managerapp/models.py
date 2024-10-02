from django.db import models

# Create your models here.
class CustomQuery(models.QuerySet):
    def admin(self):
        return self.filter(name="Narayan")

class CustomManager(models.Manager):
    def count_name(self):
        return self.aggregate(name_count=models.Count('name'))
    def get_queryset(self):
        return CustomQuery(self.model,using=self._db)
    def admin(self):
        return self.get_queryset().admin()
    
class PeopleName(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField(default=10)
    objects = models.Manager()
    admin_obj = CustomManager()
    
    
