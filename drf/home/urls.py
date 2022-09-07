from django.urls import path
from .views import HomeView, load_data

urlpatterns = [
    path('', HomeView.as_view({'get': 'list'}), name='home'),
    path('load_data',load_data, name='load_data')
]