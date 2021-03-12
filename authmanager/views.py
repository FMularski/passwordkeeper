from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages


def login_page(request):
    form = ExtendedUserCreationForm()

    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.pin = make_password(user.pin)
            user.save()
            messages.success(request, f'User {user.username} successfully registered.')
            return redirect('authmanager:login_page')
            
    context = {'form': form}
    return render(request, 'authmanager/login_page.html', context)
