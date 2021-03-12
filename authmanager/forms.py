from django.contrib.auth.forms import UserCreationForm
from .models import ExtendedUser
from django import forms

class ExtendedUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'nes-input'}))

    class Meta:
        model = ExtendedUser
        fields = ['username', 'email', 'password1', 'password2', 'pin']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'nes-input'}),
            'email': forms.EmailInput(attrs={'class': 'nes-input'}),
            'pin': forms.PasswordInput(attrs={'class': 'nes-input'})
        }