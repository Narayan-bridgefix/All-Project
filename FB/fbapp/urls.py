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
    path('upload/',views.upload,name='upload')
] 
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)