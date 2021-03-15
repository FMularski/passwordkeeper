from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm
from .models import Account
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods


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


@require_http_methods(['POST'])
def delete_account(request, account_id):
    if request.method == 'POST':
        account = get_object_or_404(Account, id=account_id)
        
        if request.user != account.owner:
            return HttpResponseBadRequest()
        
        account.delete()

        return redirect('home:home_page')
