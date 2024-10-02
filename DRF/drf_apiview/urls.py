from django.urls import path,include
from  .views import ListEmployee,Auth,CustomAuthToken,TestF
# from rest_framework.authtoken import views

urlpatterns = [
    path('',ListEmployee.as_view()),
    path('<int:pk>',ListEmployee.as_view()),
    path('auth/',Auth.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('test/',TestF.as_view())
]  