from .models import Contact, Booking
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title', 'name', 'email', 'body', 'image',)
