from django import forms

class Updateform(forms.Form):
    firstname=forms.CharField(max_length=100, required=True,help_text="enter text",error_messages={
               'required': 'Please enter your name'
                })
    lastname=forms.CharField(max_length=100, required=True)
    password=forms.CharField(max_length=100, required=True)
    username=forms.CharField(max_length=100, required=True)
    
    