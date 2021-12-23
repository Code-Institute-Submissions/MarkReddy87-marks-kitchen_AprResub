from django import forms
from .models import Contact, Booking


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title', 'name', 'email', 'body', 'image',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('party_name', 'user_name', 'booking_date', 'booking_time', 'num_of_guests', 'email', 'phone',)
