from rest_framework import serializers
from .models import Employee,TestS

class EmployeeSerializer(serializers.ModelSerializer):
    # bool = serializers.BooleanField()
    class Meta:
        model = Employee
        fields = ['name','org_id']
        

class TestSerialize(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    
    # def create(self, validated_data):
    #     return TestS.create(**validated_data)
    
    def validate_content(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
    
    
from .models import Comment
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
    
    
    
class TestFields(serializers.Serializer):
    bool = serializers.BooleanField(default=True)
    
    
    
# from .models import Album   
# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']

from .models import Album   ,Track
# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='title'
#      )

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
        


from .models import CustomerReportRecord
class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReportRecord
        fields = "__all__"      