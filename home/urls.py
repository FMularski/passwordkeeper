from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('delete_account/<int:account_id>/', views.delete_account, name='delete_account'),
    path('edit_account/<int:account_id>/', views.edit_account, name='edit_account'),
    path('ajax/get_account_password/<int:account_id>/', views.get_account_password, name='get_account_password')
]
