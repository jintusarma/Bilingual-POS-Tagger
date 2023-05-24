from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *
import uuid
from .utils import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def register(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        # username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=email,password=password1,first_name=f_name,last_name=l_name)
        user.save()
        messages.success(request,"Your Accont has been successfully created")
        p_obj=Profile.objects.create(
            user = user,
            email_token = str(uuid.uuid4())
        )
        send_mail_token(email, p_obj.email_token)
        # print(f_name)
        return redirect('login')
    else:
        print("Not")
        return render(request,'login/register.html')
    

def verify(request,token):
    try:
        obj = Profile.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        return HttpResponse("Your Account Verified")
    except Exception as e:
        return HttpResponse("invalid token")

    
def login_as_bodo(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        # user = authenticate(username = email, password = password1)
        user = authenticate(username=email,password=password1,)
        print("user",user)
        if user is not None:
            login(request, user)
            fname = email
            print(fname)
            # return render(request,'home.html',{'fname':fname})
            return redirect('bodo-home')
                    
        else:
            print("error")
            messages.error(request,"Bad Credential")
            return redirect('login')
    return render(request,'login/login.html')

def login_as_assamese(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        # user = authenticate(username = email, password = password1)
        user = authenticate(username=email,password=password1,)
        print("user",user)
        if user is not None:
            login(request, user)
            fname = email
            print(fname)
            # return render(request,'home.html',{'fname':fname})
            return redirect('as-home')
                    
        else:
            print("error")
            messages.error(request,"Bad Credential")
            return redirect('login')
    return render(request,'login/login.html')

def logout_as(request):
    logout(request)
    return redirect('main')