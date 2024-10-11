from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Home_Page(request):
    return render(request,'index.html')

def Register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname = request.POST.get('lname')
        uname=request.POST.get('uname')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')

        new_user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            email=email,
            username=uname,
            password=pwd
        )
        new_user.save()
        return redirect('login')

    return render(request, 'register.html')

def Login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd = request.POST.get('pwd')

        # user=authenticate(username=uname,password=pwd) # correct
        user = authenticate(request,username=uname, password=pwd)
        if user is not None:
            login(request,user)
            return  redirect('home')
        else:
            return HttpResponse('Error,User does not exist')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
