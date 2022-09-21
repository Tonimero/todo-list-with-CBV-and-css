from queue import Empty
from django.contrib import messages
from django.shortcuts import render, redirect
#the login functionality
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

#login Views

def loginUserdata(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #authenticate the user
        if user is not None:
            login(request, user)
            return redirect ('index')
        else:
            messages.success(request, ("Invalid Username or Password"))
            return redirect('login')
    else:
        return render(request, 'folder/login.html')
    
    
    
def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if not User.objects.filter(username=username, email=email).exists():
            if len(password) > 8 and not None:
                user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Registered Successfully')
                return redirect('login')
            else:
                messages.success(request,'Password too short. must be up to 8 characters including numbers')
                return redirect('register')
        else:
            messages.success( 'Username or Email exists') 
            return redirect('register')  
    else:
        return render(request, 'folder/register.html')     

# Create your views here.
