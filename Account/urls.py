from django.urls import path
from . import views

app_name = 'Account'

urlpatterns = [
    path('', views.Profile, name='Profile'),
    path('giris-yap', views.Login, name='Login'),
    path('cikis-yap', views.Logout, name='Logout')
]