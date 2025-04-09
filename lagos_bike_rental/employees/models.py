
# Create your models here.
from django.db import models
from users.models import CustomUser

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)