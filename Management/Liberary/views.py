from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import Books,Library,Admin
from .serializer import UserSerializer,BooksSerializer,LibrarySerializer

# Creating Token while Registration by signal
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def generate_token(sender,instance,created=False,**kwarg):
    if created:
        Token.objects.create(user=instance)



# Register the new User
class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            username = user_serializer.validated_data['username']
            password = user_serializer.validated_data['password']
            user = User.objects.filter(username=username).exists()
            if not user:
                user = User.objects.create(username=username)
                user.set_password(password)
                user.save()
                token,created = Token.objects.get_or_create(user=user)
                return Response({"user":"Registered Successfully","Token":token.key})
            return Response({"user":"already Exist"})
        return Response({"error":user_serializer.errors})
            
# Get Token of Existing User
class GetToken(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        if not User.objects.filter(username=username).exists():
            return Response({"error":"Incorrect Username"})
        user=authenticate(username=username,password=password)
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token":token.key})
        return Response({"error":"Incorrect Password"})
        
class BookRelatedOperation(APIView):
    def get(self,request):
        books= Books.objects.all()
        book_serializer = BooksSerializer(books,many=True)
        return Response(book_serializer.data)
    
class LibraryRelatedOperation(APIView):
    def get(self,request):
        print(request.user)
        libraries = Library.objects.all()
        library_serializer = LibrarySerializer(libraries,many=True)
        return Response(library_serializer.data)
    
    def post(self,request):
        if not Admin.objects.filter(username=request.user).exists():
            return Response({"error":"You are not Admin User To add Library Create a admin account"})
        liberary_serializer = LibrarySerializer(data=request.data)
        # admin_user = Admin.objects.get(username=request.user)
        if liberary_serializer.is_valid():
            # liberary_serializer.Library_admin=admin_user
            #add admin user to library
            liberary_serializer.save()
            return Response({"library":"Added"})
        return Response(liberary_serializer.errors)
    
    
    
