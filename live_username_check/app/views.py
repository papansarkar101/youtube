from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def check_username(request):
    username = request.POST.get('username')

    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div style="color: red"> This username already exists </div>')
    else:
        return HttpResponse('<div style="color: green"> This username is available </div>')