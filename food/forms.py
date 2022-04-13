""" relevant imports below """
from django import forms
from .models import Contact, Booking


class ContactForm(forms.ModelForm):
    """ Registering fields for Contact form """
    class Meta:
        """ meta class for contact form """
        model = Contact
        fields = ('title', 'email', 'body', 'image',)


class DateInput(forms.DateInput):
    """ Custom class for date widget """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """ Custom class for time widget """
    input_type = 'time'


class BookingForm(forms.ModelForm):
    """ Registering fields for Booking form """
    class Meta:
        """ meta class for booking form """
        model = Booking
        fields = ('party_name', 'booking_date', 'booking_time',
                  'num_of_guests', 'email', 'phone',)
        widgets = {
            'booking_date': DateInput(),
            'booking_time': TimeInput()
        }
