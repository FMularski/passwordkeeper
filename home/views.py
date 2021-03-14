from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth.hashers import make_password


def home_page(request):
    form = AccountForm()

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.password = make_password(account.password)
            account.owner = request.user
            account.save()
            return redirect('home:home_page')

    context = {'form': form}
    return render(request, 'home/home_page.html', context)