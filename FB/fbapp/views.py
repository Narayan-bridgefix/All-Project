from datetime import datetime
from fbapp.models import User,Post_Image,Like_Image,Comment_Image,Request_User
from django.contrib import messages
from  django.http import HttpResponse, HttpResponseRedirect,JsonResponse
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
    if request.method=='POST':
        form = UserPost(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserPost()
    images=Post_Image.objects.all()
    get_comment=Comment_Image.objects.filter()
    return render(request,'fbapp/index.html',{'form':form,'image':images,"comments":get_comment})

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


def likecount(request):
    if request.method=='POST':
        imageid=request.POST.get('image')
        image=Post_Image.objects.get(pk=imageid)
        user_id=request.user.id
        get_user=User.objects.get(pk=user_id)
        image_check= Like_Image.objects.filter(user=user_id,post_id=imageid).exists()
        if not image_check:
            user=Like_Image.objects.create(post_id=image,user=get_user)
            image.like+=1
            image.save()
            user.save()
        return HttpResponseRedirect('/')
    return redirect('/')


def unlikecount(request):
    if request.method=='POST':
        imageid=request.POST.get('image')
        image=Post_Image.objects.get(pk=imageid)
        user_id=request.user.id
        get_user=User.objects.get(pk=user_id)
        image_check= Like_Image.objects.filter(user=user_id,post_id=imageid).exists()
        if image_check:
            user=Like_Image.objects.filter( post_id=image,user=get_user)
            image.like-=1
            image.save()
            user.delete()
        return redirect('/')
    return redirect('/')

def comment(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        print(comment)
        imageid=request.POST.get('imageid')
        get_user=User.objects.get(pk=request.user.id)
        get_image=Post_Image.objects.get(pk=imageid)
        if comment:
            comment_save= Comment_Image.objects.create(post_id=get_image,comment=comment,user=get_user)
            comment_save.save()
        return redirect('/')
        # get_comment=Comment_Image.objects.all()
        # return render(request,'fbapp/index.html')
    return redirect('/')    



def add_comment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        imageid=request.POST.get('imageid')
        get_user=User.objects.get(pk=request.user.id)
        get_post=Post_Image.objects.get(pk=imageid)
        add_comment= Comment_Image.objects.create(post_id=get_post,user=get_user,comment=comment)
        add_comment.save()
        return JsonResponse({"comment":comment})


def upload(request):
    if request.method=="POST":
        form = UserPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # img_object = form.instance
            # print(img_object)
        return redirect('/index/')
    return redirect('/index/')



def user_request(request):
    user=User.objects.exclude(pk=request.user.id,)
    remove_this_user=Request_User.objects.filter(request_to=request.user.id,request_accepted=True)
    print(remove_this_user.values())
    return render(request,'fbapp/userrequest.html',{"user":user,"remove_user":remove_this_user})

def send_request(request):
    if request.method=="POST":
        print("getting request")
        userid=request.POST.get('userid')
        get_user=User.objects.get(pk=userid)
        get_requested_by_user=User.objects.get(pk=request.user.id)
        check_user_exist=Request_User.objects.filter(request_by=get_requested_by_user,request_to=get_user).exists()
        if not check_user_exist:
            create_request=Request_User.objects.create(request_by=get_requested_by_user,request_to=get_user)
            create_request.save()
        return redirect('/user_request/')

def list_all_request(request):
    all_request=Request_User.objects.filter(request_to=request.user.id,request_accepted=False)
    print(all_request)
    return render(request,'fbapp/list_all_request.html',{"user_request":all_request})

def confirm_request(request):
    if request.method=="POST":
        user_id=request.POST.get('user_id')
        request_confirm=Request_User.objects.get(request_by=user_id,request_to=request.user.id)
        request_confirm.request_accepted=True
        request_confirm.save()
            
        # request_confirm.save()
    return redirect('/list_all_request/')

def all_friend(request):
    friend= Request_User.objects.filter(request_to=request.user.id,request_accepted=True)
    return render(request,'fbapp/all_friend.html',{"friend":friend})

def unfollow(request):
    if request.method=="POST":
        user_id=request.POST.get('user_id')
        user_to_delete=Request_User.objects.get(request_by=user_id,request_to=request.user.id,request_accepted=True)

        user_to_delete.delete()
    return redirect('/all_friend/')