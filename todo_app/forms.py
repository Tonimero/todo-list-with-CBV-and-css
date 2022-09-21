from django import forms
from .models import *

class userLoginForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'password']