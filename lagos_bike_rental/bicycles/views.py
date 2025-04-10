

# Create your views here.
# bicycles/views.py
from django.shortcuts import render
from .models import Bicycle  # Assuming you have a Bicycle model

def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycles/bicycle_list.html', {'bicycles': bicycles})
