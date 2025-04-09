
# Register your models here.
from django.contrib import admin
from .models import CustomUser

# Register the CustomUser model in the admin
admin.site.register(CustomUser)
