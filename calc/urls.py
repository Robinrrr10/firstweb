from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('home2/', views.home2, name='home2'),
    path('home3/', views.home3, name='home3'),
    path('home4/', views.home4, name='page4'),
    path('addition/', views.addPage, name='add'),
    path('addition/addResult', views.performAddition, name='addres'),
    path('sign/', views.signPage, name='signinpage'),
    path('sign/verify', views.dosign, name='dosignin')
    ]