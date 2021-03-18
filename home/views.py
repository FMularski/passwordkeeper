from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm
from .models import Account
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.contrib import messages


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
        
        if request.user != account.owner:   # prevent deleting other users' accounts
            return HttpResponseBadRequest()
        
        account.delete()

        return redirect('home:home_page')


@require_http_methods(['POST'])
def edit_account(request, account_id):
    if request.method == 'POST':
        account_to_edit = get_object_or_404(Account, id=account_id)

        if request.user != account_to_edit.owner: # prevent editing other users' accounts
            return HttpResponseBadRequest()

        form = AccountForm(request.POST)
        if form.is_valid():
            account_obj_form_form = form.save(commit=False)
            account_to_edit.title = account_obj_form_form.title
            account_to_edit.login = account_obj_form_form.login
            account_to_edit.email = account_obj_form_form.email
            account_to_edit.password = account_obj_form_form.password

            account_to_edit.save()
        else:
            for field in form.errors:
                for msg in form.errors[field]:
                    messages.error(request, msg)



    
        return redirect('home:home_page')
        
