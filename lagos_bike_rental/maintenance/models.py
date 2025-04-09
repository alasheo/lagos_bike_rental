
# Create your models here.
from django.db import models
from bicycles.models import Bicycle
from users.models import CustomUser

class Maintenance(models.Model):
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    issue = models.TextField()
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='open')
    reported_at = models.DateTimeField(auto_now_add=True)