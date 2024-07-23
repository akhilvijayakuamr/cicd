from django.shortcuts import render,redirect
from .models import User
from .forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from  . import views

# Create your views here.

def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context={'form':form}
    return render(request,'myapp/register.html',context)



def home(request):
    return render(request,'myapp/home.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home')
    
    else:

        if request.method=='POST':
            name=request.POST.get('Username')
            pwd=request.POST.get('Password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return redirect('/login')
    return render(request,'myapp/login.html')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')

    return render(request,'myapp/home.html')
    
