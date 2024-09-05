from django.shortcuts import render

def login_page(request):
    return render(request, 'permission_app/login.html')