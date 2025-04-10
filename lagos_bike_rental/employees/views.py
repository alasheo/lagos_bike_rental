from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def employee_home(request):
    return HttpResponse("Employee Home Page")
