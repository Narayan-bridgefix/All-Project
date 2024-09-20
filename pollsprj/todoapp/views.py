from datetime import datetime
from todoapp.models import Tasklist,User
from django.contrib import messages
from  django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from todoapp.forms import Updateform
import pyotp
from .otp import generate_otp
from email.message import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
import time
@login_required
def index(request):
    task=Tasklist.objects.filter(user=request.user)
    return render(request,'todo/index.html',{'task':task,"user":request.user})

@login_required
def addtask(request):
    if request.method=="POST":
        task=Tasklist(user=request.user,task=request.POST["task"])
        task.save()
        return redirect('/todo/index')
    return render(request,'todo/addtask.html')

@login_required
def deletetask(request,taskid):
    task=Tasklist.objects.get(id=taskid,user=request.user)
    task.delete()
    return redirect('/todo/index/')

@login_required
def update(request,taskid):
    newtask=request.POST['task']
    Tasklist.objects.filter(pk=taskid,user=request.user).update(task=newtask)
    return redirect('/todo/index')
    
@login_required
def updatepage(request,taskid):
    task=Tasklist.objects.get(pk=taskid,user=request.user)
    return render(request,'todo/update.html',{"task":task})

def register(request):
    if request.user.is_authenticated:
        return redirect('/todo/index/')
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        fname=request.POST.get("first_name")
        lname=request.POST.get("last_name")
        user=User.objects.filter(username=username)
        
        
        
        if user.exists():
            messages.info(request,"user already exist")
            return redirect("/todo/register")
        
        # otp
        otp=pyotp.TOTP(pyotp.random_base32()).now()
        print("otp generated ",otp)
        
        c = datetime.now()
        current_time = c.strftime('%H:%M:%S')

        
        is_opt_expire=False
        # user=User.objects.create_user(username=username,first_name=fname,last_name=lname)
        # user.otp=otp
        # user.set_password(password)
        # user.save()
        
        #send otp
        send_mail(
                'Email Verification OTP',
                f'Your OTP for email verification is: {otp}',
                settings.EMAIL_HOST_USER,
                [username],
                fail_silently=False, auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD,connection=None, html_message=None

            )
        
        return render(request,'todo/otp.html',{"username":username,"password":password,"first_name":fname,"last_name":lname,"otp":otp,"is_opt_expire":is_opt_expire,"time":current_time})
    return render(request,'todo/register.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/todo/index/')
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        checkbox=request.POST.get('checkbox')
        user=User.objects.filter(username=username).exists()
        if not user:
            messages.error(request,"Invalid username")
            return redirect('/todo/')
        
        #using otp
        # user_otp=request.POST.get('otp')
        # get_otp_user=User.objects.get(username=username)
        
        # if user_otp==get_otp_user.otp:
        #     login(request,get_otp_user)
        #     return redirect('/todo/index/')
        # else:
        #     messages.error(request,"Invalid OTP")
        #     return redirect('/todo/')
        
        #using password
        user=authenticate(username=username,password=password)
        # if checkbox:
        #     User.objects.filter(username=username).update(remember_me=checkbox)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/todo/')
        else:
            login(request,user)
            if not checkbox:
                request.session.set_expiry(0)
            return redirect('/todo/index/')
    return render(request,'todo/login.html')

def logout_page(request):
    logout(request)
    return redirect('/todo/')

def test(request):
    otp=pyotp.TOTP("base32secret3232")
    print(otp.now())
    if request.method=="POST":
        form=Updateform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            fname=form.cleaned_data['firstname']
            lname=form.cleaned_data['lastname']
            user=User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)
            user.save()
            return redirect('/todo/test/')
    return render(request,'todo/test.html' ,{"form":Updateform(),"otp":otp})

def sendmail(request):
    email='narayanpunase16@gmail.com'
    email_otp = generate_otp()
    send_mail(
            'Email Verification OTP',
            f'Your OTP for email verification is: {email_otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False, auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD,connection=None, html_message=None

        )
    return HttpResponse("mail send")

def generateotp(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    fname=request.POST.get("first_name")
    lname=request.POST.get("last_name")
    user=User.objects.filter(username=username)
    # user.otp=otp
    # user.save()
    otp=pyotp.TOTP(pyotp.random_base32()).now()
    print("otp generated ",otp)
    
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
    return render(request,"todo/otp.html" , {"username":username,"password":password,"first_name":fname,"last_name":lname,"otp":otp,"is_opt_expire":is_opt_expire,"time":current_time})
     
def otp(request):
    if request.method=="POST":
        return render(request,'todo/otp.html')
    return redirect('/todo/register/')
    
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
        # return HttpResponse(is_opt_expire)
        # user=User.objects.get(username=username)
        # if verified_otp==otp and not is_opt_expire:
        print(is_opt_expire,"otp:",otp,"verified otp",verified_otp)
        if is_opt_expire=="False" and otp==verified_otp:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname)
            user.set_password(password)
            user.save()
            user_logged=authenticate(username=username,password=password)
            login(request,user_logged)
            return redirect('/todo/index/')
        elif is_opt_expire=="true":
            messages.error(request,"OTP Expired Please Re-Generate")
            # return redirect('/todo/otp/')
            return render(request,'todo/otp.html',{"username":username,"password":password,"first_name":firstname,"last_name":lastname,"otp":verified_otp,"is_opt_expire":is_opt_expire,"time":current_time})
        else:
            messages.error(request,"Invalid OTP")
            # return redirect('/todo/otp/')
            return render(request,'todo/otp.html',{"username":username,"password":password,"first_name":firstname,"last_name":lastname,"otp":verified_otp,"is_opt_expire":is_opt_expire,"time":current_time})
    return redirect('/todo/register/')   