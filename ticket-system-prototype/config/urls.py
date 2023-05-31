from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('authentication.urls', namespace='authentication')),
    path('tickets/', include('tickets.urls', namespace='tickets')),
    path('users/', include('users.urls', namespace='users')),
]
