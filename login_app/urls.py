from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', loginUserdata, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', registerUser, name='register'),
] 