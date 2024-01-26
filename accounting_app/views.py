from django.shortcuts import render
from .models import Service

def landing(request):
    return render(request, 'landing.html')
