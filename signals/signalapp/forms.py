from django import forms
from signalapp.models import User

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ('name', 'email')