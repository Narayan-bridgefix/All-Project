from django import forms
from .models import Post_Image

class UserPost(forms.ModelForm):
    class Meta:
        model = Post_Image
        fields = ['image']
        
