from django.db import models
from django.contrib.auth.models import User


class Booking (models.Model):
    party_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    booking_date = models.DateField(blank=False, null=False)
    booking_time = models.TimeField(blank=False, null=False)
    num_of_guests = models.IntegerField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
