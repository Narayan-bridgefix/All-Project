from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name="register"),
    path('',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('otp/',views.otp,name="otp"),
    path('validateotp/',views.validate_otp,name="validateotp"),
    path('generateotp/',views.generateotp,name="generateotp"),
    path('upload/',views.upload,name='upload'),
    path('likecout/',views.likecount,name='likecout'),
    path('unlikecout/',views.unlikecount,name='unlikecout'),
    path('comment/',views.comment,name="comment"),
    path('addcomment/',views.add_comment,name="addcomment"),
    path('user_request/',views.user_request,name="user_request"),
    path('send_request',views.send_request,name="send_request"),
    path("list_all_request/",views.list_all_request,name="list_all_request"),
    path("confirm_request/",views.confirm_request,name="confirm_request"),
    path("all_friend/",views.all_friend,name="all_friend"),
    path("unfollow/",views.unfollow,name="unfollow"),
] 
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)