from django.shortcuts import render
from .forms import AccountForm
from .models import Account


def home_page(request):
    form = AccountForm()

    context = {'form': form}
    return render(request, 'home/home_page.html', context)