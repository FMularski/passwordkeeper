from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import ChangePasswordForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import update_session_auth_hash


@login_required(login_url='authmanager:login_page')
def settings_page(request):
    password_form = ChangePasswordForm()
    context = {'password_form': password_form}
    return render(request, 'accountsettings/settings.html', context)


@login_required(login_url='authmanager:login_page')
def log_out(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('authmanager:login_page')


@require_http_methods(['POST'])
def change_password(request):
    if request.method == 'POST':
        password_form = ChangePasswordForm(request.POST)
        if password_form.is_valid():
            old_password = password_form.cleaned_data.get('old_password')

            if check_password(old_password, request.user.password):
                pin = password_form.cleaned_data.get('pin')

                if check_password(pin, request.user.pin):
                    new_password = password_form.cleaned_data.get('new_password')
                    request.user.set_password(new_password)
                    request.user.save()
                    update_session_auth_hash(request, request.user) # prevents from logout after password change
                    messages.success(request, 'Password has been changed successfully.')
                else:
                    messages.error(request, 'Invalid pin.')
            else:
                messages.error(request, 'Invalid old password.')
        else:
            for field in password_form.errors:
                for msg in password_form.errors[field]:
                    messages.error(request, msg)
        
        return redirect('settings:settings')
