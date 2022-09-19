from django.urls import path

from .views import *

urlpatterns = [
    
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('', TaskList.as_view(), name='index'),
    
    
]
