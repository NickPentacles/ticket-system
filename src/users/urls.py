from django.urls import path

from . import views


app_name = 'users'


urlpatterns = [
    path('', views.redirection, name='redirection'),
    path('register/', views.RegisterUser.as_view(), name='register_user'),
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('users/', views.UserList.as_view(), name='list_user'),
    path('users/<int:pk>/', views.EditUser.as_view(), name='edit_user'),
]
