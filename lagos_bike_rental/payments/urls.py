# payments/urls.py
from django.urls import path
from . import views
print("payments/urls.py loaded")  # 👈 Add this at the top

urlpatterns = [
    path('pay/', views.payment_view, name='payment_view'),
]
