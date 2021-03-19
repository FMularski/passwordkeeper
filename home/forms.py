from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        
        if not title:
            raise forms.ValidationError('Title is required.')
        
        pin = cleaned_data.get('pin')
        if not pin:
            raise forms.ValidationError('PIN is required.')
        
        login = cleaned_data.get('login')
        email = cleaned_data.get('email')

        if not (login or email):
            raise forms.ValidationError('Either login or email is required.')

        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm')

        if password != confirm:
            raise forms.ValidationError('The two password fields didn\'t match.')

        return cleaned_data

    confirm = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    pin = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    class Meta:
        model = Account
        exclude = ['owner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'nes-input'}),
            'login': forms.TextInput(attrs={'class': 'nes-input'}),
            'email': forms.EmailInput(attrs={'class': 'nes-input'}),
            'password': forms.PasswordInput(attrs={'class': 'nes-input'})
        }
