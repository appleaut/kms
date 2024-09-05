from django.urls import path
from authen_app import views

urlpatterns = [
    path('', views.login_page, name='home_page'),
]