from .models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
