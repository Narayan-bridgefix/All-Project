from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializer import EmployeeSerializer,Test
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
# Create your views here.


#testing fields
class TestF(APIView):
    #  throttle_classes=[UserRateThrottle]
     def post(self,request):
        serialize_emp = Test(data=request.data)
        if serialize_emp.is_valid():
            # serialize_emp.save()
            # print(serialize_emp.data)
            return Response(serialize_emp.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialize_emp.errors)





class ListEmployee(APIView):

    
    def get(self,request,pk=None):
        if pk:
            emp=Employee.objects.get(pk=pk)
            serialize_emp = EmployeeSerializer(emp)
        else:
            emp = Employee.objects.all()
            serialize_emp = EmployeeSerializer(emp,many=True)
        return Response(serialize_emp.data)
    
    def post(self,request):
        serialize_emp = EmployeeSerializer(data=request.data)
        if serialize_emp.is_valid():
            serialize_emp.save()
        return Response(serialize_emp.data,status=status.HTTP_201_CREATED)
    
    def delete(self,request,pk):
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response("Employee Deleted")
    
    def put(self,request,pk):
        emp = Employee.objects.get(pk=pk)
        serialize_emp = EmployeeSerializer(emp,data=request.data)
        if serialize_emp.is_valid():
            serialize_emp.save()
        return Response(serialize_emp.data)
    
    
    
    
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
#Token generation by TOKEN model
class Auth(APIView):
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    # permission_classes = [IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly]
    
    def post(self,request):
        user = authenticate(username=request.data['username'],password=request.data['password'])
        if user:
            token,c = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({'error':'Invalid Credential'})
        
    def get(self,request):
        return Response({"user":request.user.username})
    
    
#Token generation by Obtainauthtoken class and also customize  
from rest_framework.authtoken.views import ObtainAuthToken
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={"request":request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'username':user.username,
            'created':created
            
        })
        
        
#Token generation by Signals
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance,created=False,**kwarg):
    if created:
        Token.objects.create(user=instance)