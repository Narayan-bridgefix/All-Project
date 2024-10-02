from django.contrib import admin
from .models import Post_Image,User,Comment_Image,Request_User
# Register your models here.
admin.site.register(Post_Image)
# admin.site.register(User)
admin.site.register(Comment_Image)
admin.site.register(Request_User)