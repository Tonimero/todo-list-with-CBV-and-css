from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *







# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'folder/index.html'
    context_object_type = 'task'
