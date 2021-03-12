from django.shortcuts import render


def login_page(request):
    context = {}
    return render(request, 'authmanager/login_page.html', context)
