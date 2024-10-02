from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from signalapp.forms import UserForm

def create_user(request):
   # If the form is submitted, save the user. Otherwise, just create an empty form.
   if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
         form.save()
   else:
      form = UserForm()
      # send the base.html file on the response.
   return render(request, 'base.html', {'form': form})