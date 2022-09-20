from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy


#the login functionality
from django.contrib.auth.views import LoginView
from django.contrib.auth import login




#login Views

class loginUser(LoginView):
    template_name = 'folder/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')



# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'folder/index.html'
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    template_name = 'folder/create.html'
    fields = ['title', 'description']
    context_object_name = 'tasks'
    success_url = reverse_lazy('index') 

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'folder/update.html'
    fields = ['title', 'description']
    context_object_name = 'tasks'
    success_url = reverse_lazy('index') 
    

class TaskDelete(DeleteView):
    model = Task
    template_name = 'folder/delete.html'
    success_url = reverse_lazy('index') 
    context_object_name = 'delete'