from django import forms
from .models import UserData

class UserPost(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['post']
        
