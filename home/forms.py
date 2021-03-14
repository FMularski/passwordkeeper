from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'nes-input'}),
            'login': forms.TextInput(attrs={'class': 'nes-input'}),
            'email': forms.EmailInput(attrs={'class': 'nes-input'}),
            'password': forms.PasswordInput(attrs={'class': 'nes-input'})
        }