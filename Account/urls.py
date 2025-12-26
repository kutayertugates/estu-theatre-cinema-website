from django.urls import path
from . import views

app_name = 'Account'

urlpatterns = [
    path('giris-yap', views.Login, name='login')
]