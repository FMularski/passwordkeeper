from django import forms
from django.core.exceptions import ValidationError


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    new_password = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    confirm_password = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    pin = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if old_password == new_password:
            raise ValidationError('Old password and new password cannot be the same.')

        if new_password != confirm_password:
            raise ValidationError('Invalid new password confirmation.')

        return cleaned_data


class ChangePinForm(forms.Form):
    old_pin = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    new_pin = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    password = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'nes-input'}))

    def clean(self):
        cleaned_data = super().clean()
        old_pin = cleaned_data.get('old_pin')
        new_pin = cleaned_data.get('new_pin')
        
        if old_pin == new_pin:
            raise ValidationError('Old PIN and new PIN cannot be the same.')

        return cleaned_data