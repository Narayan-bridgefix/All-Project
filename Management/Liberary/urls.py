from django.urls import path
from .views import RegisterUser,GetToken,BookRelatedOperation,LibraryRelatedOperation

urlpatterns = [
    path('register/',RegisterUser.as_view()),
    path('token/',GetToken.as_view()),
    path('book/',BookRelatedOperation.as_view()),
    path('library/',LibraryRelatedOperation.as_view()),
]
