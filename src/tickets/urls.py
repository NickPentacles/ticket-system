from django.urls import path

from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.MyTickets.as_view(), name='my_tickets'),
    path('list/', views.AllTickets.as_view(), name='all_tickets'),
    path('list/<int:pk>/', views.EditTicket.as_view(), name='edit_tickets'),
    path('create/', views.CreateTicket.as_view(), name='create_tickets'),
    path('delete/<int:pk>/', views.DeleteTicket.as_view(), name='delete_tickets'),
    path('pending/', views.PendingTickets.as_view(), name='pending_tickets'),
    path('complete/<int:pk>/', views.complete_ticket, name='complete_tickets')
]
