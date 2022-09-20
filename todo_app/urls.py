from django.urls import path

from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', loginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    
    path('delete/<slug:slug>/', TaskDelete.as_view(), name='delete'),
    path('update/<slug:slug>/', TaskUpdate.as_view(), name='update'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('', TaskList.as_view(), name='index'),
]