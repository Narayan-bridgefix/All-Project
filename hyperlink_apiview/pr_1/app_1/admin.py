from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Student)
admin.site.register(ref)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Track)
admin.site.register(Album)
