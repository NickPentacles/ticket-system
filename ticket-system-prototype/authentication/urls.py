from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.redirection, name='redirection'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout')
]
