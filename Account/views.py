from django.shortcuts import render

def Login(request):
    return render(request, 'Account/login.html')

