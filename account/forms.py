from django import forms
from .models import User, UserManager

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

