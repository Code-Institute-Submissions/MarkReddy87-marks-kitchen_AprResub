from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Booking (models.Model):
    party_name = models.CharField(max_length=20)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_name", default=False)
    booking_date = models.DateField(blank=False, null=False)
    booking_time = models.TimeField(blank=False, null=False)
    num_of_guests = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.party_name


class Contact (models.Model):
    title = models.CharField(max_length=200, unique=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contact_from")
    email = models.EmailField()
    body = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
