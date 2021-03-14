from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    confirm = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    class Meta:
        model = Account
        exclude = ['owner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'nes-input'}),
            'login': forms.TextInput(attrs={'class': 'nes-input'}),
            'email': forms.EmailInput(attrs={'class': 'nes-input'}),
            'password': forms.PasswordInput(attrs={'class': 'nes-input'})
        }