from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name="Home"),
    path('login', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('raise', views.Raise, name="raise"),
    path('ticket', views.TicketID, name="ticket"),
    path('send', views.Send, name="send"),
    path('getMessages/<str:room>/', views.GetMessage, name="getMessages"),
    path('transaction', views.Transaction, name="transaction"),
    # path('savings', views.Savings, name="savings"),
    # path('loan', views.Loan, name="loan"),
    # path('demat', views.Demat, name="demat"),
    
]