
# Create your models here.
from django.db import models

class Bicycle(models.Model):
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('rented', 'Rented')], default='available')
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} - {self.status}"