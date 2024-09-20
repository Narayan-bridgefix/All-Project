from django.urls import path , include
from todoapp import views
urlpatterns = [
    path('index/',views.index,name="index"),
    path('addtask/',views.addtask,name="addtask"),
    path('delete/<int:taskid>',views.deletetask,name="delete"),
    path('updatepage/<int:taskid>',views.updatepage,name="updatepage"),
    path('update/<int:taskid>',views.update,name="update"),
    path('register/',views.register,name="register"),
    path('',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('test/',views.test,name="test"),
    path('sendmail/',views.sendmail,name="sendmail"),
    path('generateotp/',views.generateotp,name="generateotp"),
    path('otp/',views.otp,name="otp"),
    path('validateotp/',views.validate_otp,name="validateotp")
]