from django.urls import path
from . import views


app_name = 'settings'

urlpatterns = [
    path('', views.settings_page, name='settings'),
    path('logout/', views.log_out, name='log_out'),
    path('change_password/', views.change_password, name='change_password')
]
