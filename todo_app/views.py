from django.shortcuts import render, redirect
from multiprocessing import context
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import *


#the login functionality
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'folder/index.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user) 
        context['count'] = context['task'].filter(completed=False).count()
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'folder/create.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('index') 
    
    def form_valid(self, form):
        form.instance.user = self.request.user #making sure the logged in user doesnt see other users when creating tasks
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'folder/update.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('index') 
    

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'folder/delete.html'
    success_url = reverse_lazy('index') 
    context_object_name = 'delete'