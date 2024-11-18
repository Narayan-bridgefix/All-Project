from django.contrib import admin
from .models import Employee
# Register your models here.

# admin.site.register(Employee)



from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token
TokenAdmin.raw_id_fields=['user']
admin.site.register(Token)


from import_export import resources
from .models import Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
# admin.site.register(Person)

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass