from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework.parsers import JSONParser
from rest_framework.renderers import StaticHTMLRenderer,JSONRenderer,TemplateHTMLRenderer
from rest_framework.decorators import action
from .renderer import PlainTextRenderer,JPEGRenderer
# from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication
# Create your views here.
class EmployeeCRUD(ViewSet):
    # parser_classes=[JSONParser]
    # renderer_classes=[PlainTextRenderer]
    # permission_classes =[DjangoModelPermissions]
    # authentication_classes=[]
    queryset = Employee.objects.all()

    def list(self,request):
        serialize_data = EmployeeSerializer(self.queryset,many=True)
        return Response(serialize_data.data)
    
    def retrieve(self,request,pk):
        emp = self.queryset.get(pk=pk)
        serialize_data = EmployeeSerializer(emp)
        return Response(serialize_data.data)
      
    def create(self,requset):
        serialize_data = EmployeeSerializer(data=requset.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data)

    def destroy(self,request,pk):
        
        # emp = self.queryset.get(pk=pk)
        # emp.delete()
        emp = self.queryset.get(pk=pk)
        serialize_data = EmployeeSerializer(emp)
        if serialize_data.is_valid():
            serialize_data.delete()
        return Response("Employee Deleted")
    
    def update(self,request,pk):
        emp = self.queryset.get(pk=pk)
        serialize_data = EmployeeSerializer(emp,data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data)
        
    @action(methods=['GET'],detail=False)
    def simple_html_view(self,request):
        data = '<html><body><h1>Hello, world</h1></body></html>'
        return Response({"data":data})
     
     
class EmpView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # def destroy(self,request,pk):
    #     emp = self.queryset.get(pk=pk)
    #     emp.delete()
    #     return Response("Employee Deleted")
    # def retrieve(self,request,pk):
    #     emp = self.queryset.get(pk=pk)
    #     serialize_data = EmployeeSerializer(emp)
    #     return Response(serialize_data.data)
    # def list(self,request):
    #     serialize_data = EmployeeSerializer(self.queryset,many=True)
    #     return Response(serialize_data.data)
from rest_framework.views import APIView
class TestRender(APIView):
    # renderer_classes=[]
    template_name = 'index.html'
    def get(self, request):
        profile = Employee.objects.get(pk=2)
        serializer = EmployeeSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})
    
    


