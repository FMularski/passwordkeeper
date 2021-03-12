from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


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


@require_http_methods(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse(request.user)
        else:
            messages.error(request, 'Username or password invalid.')
            return redirect('authmanager:login_page')