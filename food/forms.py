""" relevant imports below """
from django import forms
from .models import Contact, Booking


class ContactForm(forms.ModelForm):
    """ Registering fields for Contact form """
    class Meta:
        """ meta class for contact form """
        model = Contact
        fields = ('title', 'name', 'email', 'body', 'image',)


class BookingForm(forms.ModelForm):
    """ Registering fields for Booking form """
    class Meta:
        """ meta class for booking form """
        model = Booking
        fields = ('party_name', 'user_name', 'booking_date', 'booking_time',
                  'num_of_guests', 'email', 'phone',)
