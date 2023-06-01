from django.urls import path

from . import views


app_name = 'users'


urlpatterns = [
    path('', views.redirection, name='redirection'),
    path('register/', views.RegisterUser.as_view(), name='register_users'),
    path('login/', views.LoginUser.as_view(), name='login_users'),
    path('logout/', views.logout_user, name='logout_users'),
    path('users/', views.UserList.as_view(), name='all_users'),
    path('users/<int:pk>/', views.EditUser.as_view(), name='edit_users'),
]
