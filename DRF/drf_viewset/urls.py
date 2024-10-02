from django.urls import path,include
from  .views import EmployeeCRUD,EmpView,TestRender
from rest_framework.routers import DefaultRouter,SimpleRouter
# router = DefaultRouter()
# router.register(r'Emp', EmployeeCRUD)
# urlpatterns = router.urls


urlpatterns = [
    path('',EmployeeCRUD.as_view({'get': 'list'})),
    path('post/',EmployeeCRUD.as_view({'post': 'create'})),
    path('<int:pk>',EmployeeCRUD.as_view({'get': 'retrieve'})),
    path('delete/<int:pk>',EmployeeCRUD.as_view({'delete': 'destroy'})),
    path('update/<int:pk>',EmployeeCRUD.as_view({'put': 'update'})),
] 


# router = DefaultRouter()
# router.register(r'emp', EmpView)
# router.register(r'empview',EmployeeCRUD)

# urlpatterns =[path('temp/',TestRender.as_view())]+ router.urls