from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    Author_name = models.CharField(max_length=30)
    Author_subject = models.CharField(max_length=50)
    Author_code = models.IntegerField(unique=True)
    Author_qualification = models.CharField(max_length=50)
    
    
class Publisher(models.Model):
    Publisher_name = models.CharField(max_length=50)
    Publisher_code = models.IntegerField(unique=True)
    Publisher_country = models.CharField(max_length=50)
    
    
class Vendor(models.Model):
    Vendor_code = models.IntegerField(unique=True)
    Contact_no = models.IntegerField()
    
    
class Member(User):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Pincode = models.IntegerField(blank=True)
    Contact_no = models.IntegerField(blank=True)
    Member_type = models.CharField(max_length=50)
    
    
class Employee(models.Model):
    pass
    # Emp_id = models.IntegerField() = default
    # Emp_name = models.CharField(max_length=50)
    # Mobile_no = models.IntegerField()
    # Designation = models.CharField(max_length=50)
    # Employee_member = models.ManyToManyField("Member",related_name="member",blank=True)
    # Employee_admin = models.ForeignKey("Admin", on_delete=models.CASCADE,blank=True)
    
    
class Admin(models.Model):
    # Admin_id = models.IntegerField() = default 
    # Admin_user = models.ForeignKey("User", on_delete=models.CASCADE)
    Admin_name = models.CharField(max_length=50)
    Contact_no = models.IntegerField()
    
    
class Library(models.Model):
    Library_admin = models.ForeignKey("Admin", on_delete=models.CASCADE,blank=True,null=True)
    Library_name = models.CharField(max_length=50)
    Library_address = models.CharField( max_length=50)
    Contact_no = models.IntegerField()
    
    
class Books(models.Model):
    Books_author = models.ForeignKey("Author", on_delete=models.CASCADE,blank=True)
    Books_publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE,blank=True)
    Books_vendor = models.ForeignKey("Vendor",  on_delete=models.CASCADE,blank=True)
    Books_library = models.ForeignKey("Library", on_delete=models.CASCADE,blank=True)
    # Books_employee = models.ForeignKey("Employee", on_delete=models.CASCADE,blank=True)
    Books_status = models.BooleanField(default=False)
    Books_price = models.IntegerField()
        
        