from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name="Home"),
    # path('login', views.Login, name="login"),
    # path('logout/', views.Logout, name="logout"),
]