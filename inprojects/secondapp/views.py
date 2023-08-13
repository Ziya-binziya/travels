from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=user_name,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['password1']
        if pwd==pwd1:
           if User.objects.filter(username=uname).exists():
               messages.info(request,"username taken ")
               return redirect('register')
           elif User.objects.filter(email=mail).exists():
               messages.info(request,"email taken ")
               return redirect('register')
           user=User.objects.create_user(username=uname,password=pwd,first_name=fname,last_name=lname,email=mail)
           user.save();
           print('user created')
           return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect(request,'register')
        return redirect(request,'/')
    return render(request,'reg.html')
def logout(request):
    auth.logout(request)
    return redirect('/')