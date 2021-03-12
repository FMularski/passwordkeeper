from django.urls import path
from . import views


app_name = 'authmanager'

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login_user/', views.login_user, name='login_user')
]
