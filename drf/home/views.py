from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

from .data import student_data

def load_data(request):
    for i in student_data:
        student = Student(i['id'], i['first_name'], i['last_name'])
        student.save()
    return HttpResponse("Success")


class HomeView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
