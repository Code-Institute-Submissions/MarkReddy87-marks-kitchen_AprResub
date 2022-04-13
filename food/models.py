""" Relevant imports below """
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from cloudinary.models import CloudinaryField


class Booking (models.Model):
    """ Registering Booking model """
    party_name = models.CharField(max_length=20)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="user_name")
    booking_date = models.DateField(blank=False, null=False)
    booking_time = models.TimeField(blank=False, null=False)
    num_of_guests = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class for ordering """
        ordering = ['-created_on']


class Contact (models.Model):
    """ Registering Contact model """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="contact_from")
    email = models.EmailField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True,
                              default='placeholder')
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        """ Meta class for ordering """
        ordering = ['-created_on']
