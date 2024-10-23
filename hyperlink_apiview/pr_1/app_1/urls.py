from django.urls import path,include
from . views import *
urlpatterns = [
    path('student/',Student_view.as_view()),
    path('ref-detail/',Student_view.as_view()),
    
    path('ref-detail/<int:pk>',Student_view.as_view()),
    
    path('books/', BookList.as_view(), name='book-list'),
]


# from django.urls import path
# from .views import BookList

# urlpatterns = [
# ]
