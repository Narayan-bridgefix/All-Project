from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import hotel_image_view,success

urlpatterns = [
    path('image_upload/', hotel_image_view, name='image_upload'),
    path('success/', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
