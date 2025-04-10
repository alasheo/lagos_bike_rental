from django.shortcuts import render

# Create your views here.

# rentals/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Rentals!")
