from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail, BadHeaderError
import os


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')

    form = ExtendedUserCreationForm()
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.pin = make_password(user.pin)
            user.save()

            send_mail(
                subject='Welcome to Password Keeper',
                message=f'Thank you for registering {user.username}!',
                from_email=os.environ.get('EMAIL_USER'),
                recipient_list=[user.email],
                fail_silently=False,
                )

            messages.success(request, f'User {user.username} successfully registered.')
            return redirect('authmanager:login_page')

    context = {'form': form}
    return render(request, 'authmanager/login_page.html', context)
    

@require_http_methods(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home:home_page')
        else:
            messages.error(request, 'Username or password invalid.')
            return redirect('authmanager:login_page')