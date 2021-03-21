from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm
from .models import Account
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from view_helpers.home import encode_password, decode_password


def home_page(request):
    form = AccountForm()

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            
            pin = request.POST.get('pin')
            if check_password(pin, request.user.pin):
                account.password = encode_password(account.password, pin)
                account.owner = request.user
                account.save()
            else:
                messages.error(request, 'Invalid PIN.')
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
            pin = request.POST.get('pin')
            if check_password(pin, request.user.pin):
                account_obj_form_form = form.save(commit=False)
                account_to_edit.title = account_obj_form_form.title
                account_to_edit.login = account_obj_form_form.login
                account_to_edit.email = account_obj_form_form.email
                account_to_edit.password = encode_password(account_obj_form_form.password, pin)

                account_to_edit.save()
            else:
                # error when pin ivalid
                messages.error(request, 'Invalid PIN.')
        else:
            # errors when invalid form
            for field in form.errors:
                for msg in form.errors[field]:
                    messages.error(request, msg)
    
        return redirect('home:home_page')
        


def get_account_password(request, account_id):
    if request.is_ajax():
        pin = request.GET.get('pin')

        if not pin:
            messages.error(request, 'PIN is required.')
            return JsonResponse({'error': 'PIN is required.'}, status=400)

        if not check_password(pin, request.user.pin):
            messages.error(request, 'Invalid PIN.')
            return JsonResponse({'error': 'Invalid PIN.'}, status=400)

        account = Account.objects.get(pk=account_id)

        if not account:
            return JsonResponse({'error': f'Account with id: {account_id} not found.'}, status=404)

        decoded_password = decode_password(account.password, pin)
        return JsonResponse({'decodedPassword': decoded_password}, status=200)