from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('sign/', views.sign, name='sign'),
    path('signout/',  views.signout, name='signout')
    ]