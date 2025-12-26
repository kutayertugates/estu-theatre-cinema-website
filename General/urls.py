from django.urls import path
from . import views

app_name = 'General'

urlpatterns = [
    path('', views.Homepage, name='homepage')
]