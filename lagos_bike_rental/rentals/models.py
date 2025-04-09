
# Create your models here.
from django.db import models
from users.models import CustomUser
from bicycles.models import Bicycle

class Rental(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    rent_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)