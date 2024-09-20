from datetime import datetime
from fbapp.models import User,UserData
from django.contrib import messages
from  django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pyotp
from email.message import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
import time
from .forms import UserPost
@login_required
def index(request):
    # post=UserData.objects.all()
    form = UserPost()
    return render(request,'fbapp/index.html',{'form':form})

def register(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        fname=request.POST.get("first_name")
        lname=request.POST.get("last_name")
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"user already exist")
            return redirect("/register/")
        
        # otp
        otp=pyotp.TOTP(pyotp.random_base32()).now()
        print("otp generated ",otp)
        c = datetime.now()
        current_time = c.strftime('%H:%M:%S')
        is_opt_expire=False
        
        #send mail
        send_mail(
                'Email Verification OTP',
                f'Your OTP for email verification is: {otp}',
                settings.EMAIL_HOST_USER,
                [username],
                fail_silently=False, auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD,connection=None, html_message=None

            )
        
        return render(request,'fbapp/otp.html',{"username":username,"password":password,"first_name":fname,"last_name":lname,"otp":otp,"is_opt_expire":is_opt_expire,"time":current_time})
    return render(request,'fbapp/register.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        checkbox=request.POST.get('checkbox')
        user=User.objects.filter(username=username).exists()
        if not user:
            messages.error(request,"Invalid username")
            return redirect('/')
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/')
        else:
            login(request,user)
            if not checkbox:
                request.session.set_expiry(0)
            return redirect('/index/')
    return render(request,'fbapp/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')
     
def otp(request):
    if request.method=="POST":
        return render(request,'/otp.html')
    return redirect('/register/')
    
def validate_otp(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        otp=request.POST.get('otp')
        verified_otp=request.POST.get('verified_otp')
        is_opt_expire=request.POST.get('is_opt_expire')
        current_time=request.POST.get('current_time')

        if is_opt_expire=="False" and otp==verified_otp:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname)
            user.set_password(password)
            user.save()
            user_logged=authenticate(username=username,password=password)
            login(request,user_logged)
            return redirect('/index/')
        elif is_opt_expire=="true":
            messages.error(request,"OTP Expired Please Re-Generate")
            return render(request,'fbapp/otp.html',{"username":username,"password":password,"first_name":firstname,"last_name":lastname,"otp":verified_otp,"is_opt_expire":is_opt_expire,"time":current_time})
        else:
            messages.error(request,"Invalid OTP")
            return render(request,'fbapp/otp.html',{"username":username,"password":password,"first_name":firstname,"last_name":lastname,"otp":verified_otp,"is_opt_expire":is_opt_expire,"time":current_time})
    return redirect('/register/')   

def generateotp(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    fname=request.POST.get("first_name")
    lname=request.POST.get("last_name")
    user=User.objects.filter(username=username)
    
    otp=pyotp.TOTP(pyotp.random_base32()).now()
    
    
    c = datetime.now()
    current_time = c.strftime('%H:%M:%S')

    
    is_opt_expire=False
    
    send_mail(
            'Email Verification OTP',
            f'Your OTP for email verification is: {otp}',
            settings.EMAIL_HOST_USER,
            [username],
            fail_silently=False, auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD,connection=None, html_message=None

        )
    return render(request,"fbapp/otp.html" , {"username":username,"password":password,"first_name":fname,"last_name":lname,"otp":otp,"is_opt_expire":is_opt_expire,"time":current_time})

def upload(request):
    if request.method=="POST":
        form = UserPost(request.POST, request.FILES)
        import pdb;pdb.set_trace()
        print(form)
        if form.is_valid():
            form.save()
            img_object = form.instance
            print(img_object)
        # print(form.cleaned_data['post'])
        # if form.is_valid():
        #     p=UserData()
        #     p.post=form
        #     p.save()
        # p=request.POST.get('file')
        # print(p)
        # data=UserData(post=p)
        # data.post=p
        # data.save()
        return redirect('/index/')
    return redirect('/index/')



