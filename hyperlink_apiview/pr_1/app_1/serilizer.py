from rest_framework import serializers
from .models import *

class Student_serializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(many=True)
    class Meta:
        model = Student
        fields = ['name']
        
        
class Ref_serilize(serializers.ModelSerializer):
    students = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name='student-detail',lookup_field = 'name')

    class Meta:
        model = ref
        fields = '__all__'
        
        


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'url']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(many=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'url']
