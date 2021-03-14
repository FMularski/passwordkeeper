from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data.get('login')
        email = cleaned_data.get('email')

        if not (login or email):
            raise forms.ValidationError('Either login or email is required.')

        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm')

        if password != confirm:
            raise forms.ValidationError('Passwords don\'t match.')

        return cleaned_data

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