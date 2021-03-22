from django.shortcuts import render


def settings_page(request):
    context = {}
    return render(request, 'accountsettings/settings.html', context)