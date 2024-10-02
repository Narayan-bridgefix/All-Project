from django.urls import path,include
from  .views import EmployeeCRUD,ProductList,UserList,Orderlist
urlpatterns = [
    path('',EmployeeCRUD.as_view()),
    path('<int:pk>',EmployeeCRUD.as_view()),
    path('filter/',ProductList.as_view()),
    path('search/',UserList.as_view()),
    path('order/',Orderlist.as_view()),
    
] 