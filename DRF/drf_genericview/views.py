
from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee
# Create your views here.

class EmployeeCRUD(GenericAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    
    def get(self,pk=None):
        emp = self.get_object(pk=pk)
        serialize_data = self.get_serializer(emp)
        # else:
        #     emp = self.get_queryset()
        #     serialize_data = self.get_serializer(emp,many=True)
        return Response(serialize_data.data)
    
    def delete(self, request, *args, **kwargs):
        emp = self.get_object()
        emp.delete()
        return Response("Employee Deleted") 
    
    def put(self, request, *args, **kwargs):
        emp = self.get_object()
        serialize_data=EmployeeSerializer(emp,data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
        return Response(serialize_data.data)
    
    def post(self, request, *args, **kwargs):
        serialize_data= EmployeeSerializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data) 
        
        
from django_filters.rest_framework import DjangoFilterBackend
class ProductList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['org_id','name']
    
    
from rest_framework import filters
class UserList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','=org_id']
    
class Orderlist(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','org_id']
    ordering = ['name']