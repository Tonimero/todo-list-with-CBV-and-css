from django.urls import path

from .views import *

urlpatterns = [
    
    path('delete/<slug:slug>/', TaskDelete.as_view(), name='delete'),
    path('update/<slug:slug>/', TaskUpdate.as_view(), name='update'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('', TaskList.as_view(), name='index'),
    
    
]
