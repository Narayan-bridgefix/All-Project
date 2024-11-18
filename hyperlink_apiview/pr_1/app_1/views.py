from django.shortcuts import render
from . models import *
from .serilizer import *
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Student_view(APIView):
    def get(self,request,pk=None):
        if pk:
            st = ref.objects.get(id=pk)
            serilize = Ref_serilize(st,context={'request': request})
            return Response(serilize.data)
        else:
            st = ref.objects.all()
            serilize = Ref_serilize(st,many=True,context={'request': request})
            return Response(serilize.data)
        
        
        
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serilizer import BookSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True,context={'request':request})
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django.http import HttpResponse
import logging,traceback

logger = logging.getLogger('django')
# logger2 = logging.getLogger('mylogger')

def my_view(request):
    try:
        1 / 0  # Division by zero error
        return HttpResponse("done")
    except Exception as e:
        logger.error("An error occurred: %s\n%s", e, traceback.format_exc())
        return HttpResponse("error")

mylogger = logging.getLogger('mylogger')
def my_view2(request):
    try:
        1 / 0  # Division by zero error
        return HttpResponse("done")
    except Exception as e:
        mylogger.warning("Need to solve")
        mylogger.error("An error occurred: %s\n%s", e, traceback.format_exc())
        return HttpResponse("error log2")
    
from rest_framework.reverse import reverse    
from rest_framework.views import APIView
from django.utils.timezone import now

class APIRootView(APIView):
    def get(self, request):
        year = now().year
        data = {
            'year-summary-url': reverse('/testing', args=[], request=request)
        }
        return Response(data)