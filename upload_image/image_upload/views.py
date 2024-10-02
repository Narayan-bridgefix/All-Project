from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import HotelForm

# Create your views here.


def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
