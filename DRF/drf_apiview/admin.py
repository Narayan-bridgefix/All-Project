from django.contrib import admin
from .models import Employee
# Register your models here.

admin.site.register(Employee)


from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token
TokenAdmin.raw_id_fields=['user']
admin.site.register(Token)
