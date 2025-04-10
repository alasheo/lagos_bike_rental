from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def user_list(request):
    return HttpResponse("This is the user list page.")
