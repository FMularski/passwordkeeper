from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='authmanager:login_page')
def settings_page(request):
    context = {}
    return render(request, 'accountsettings/settings.html', context)


@login_required(login_url='authmanager:login_page')
def log_out(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('authmanager:login_page')