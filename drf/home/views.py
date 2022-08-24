from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

def home(request):
    pass


class HomeView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
