from django.urls import path

from . import views

app_name = 'requests'

urlpatterns = [
    path('', views.MyRequests.as_view(), name='my_requests'),
    path('list/', views.AllRequests.as_view(), name='list'),
    path('list/<int:pk>/', views.EditRequest.as_view(), name='edit'),
    path('create/', views.CreateRequest.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteUserRequest.as_view(), name='delete'),
    path('pending/', views.PendingRequests.as_view(), name='pending'),
    path('complete/<int:pk>/', views.complete_request, name='complete')
]
