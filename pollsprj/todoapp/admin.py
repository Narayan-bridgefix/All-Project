from django.contrib import admin
from todoapp.models import *
# from django.contrib.auth.models import User
# class Tasklistview(admin.ModelAdmin):
#     class Meta:
#         list_display = ["id", "task"]
admin.site.register(Tasklist)
admin.site.register(User)

