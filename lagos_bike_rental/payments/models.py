from django.db import models
from django.contrib.auth import get_user_model
from rentals.models import Rental

User = get_user_model()  # This ensures consistency across the project

# Payment model that links user and rental
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.email} for rental {self.rental.id}"
