
from django.urls import path
from .views import home, check_username

urlpatterns = [
    path('', home, name='home'),
    path('check_username', check_username, name='check_username'),
]