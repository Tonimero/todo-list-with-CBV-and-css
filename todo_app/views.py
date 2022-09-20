from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy






# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'folder/index.html'
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    template_name = 'folder/create.html'
    fields = ['title', 'description']
    context_object_name = 'task'
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