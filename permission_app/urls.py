from django.urls import path
from permission_app import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
]