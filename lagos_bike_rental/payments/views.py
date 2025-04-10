from django.shortcuts import render

# Create your views here.
# payments/views.py
from django.http import HttpResponse

def payment_view(request):
    return HttpResponse("Payment page")
