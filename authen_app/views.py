from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def login_page(request):
    return render(request, 'authen_app/login.html')