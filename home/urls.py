from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('delete_account/<int:account_id>/', views.delete_account, name='delete_account')
]
