from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import generic, View
from .models import Contact, Booking
from .forms import ContactForm


class ShowMenu(generic.ListView):
    template_name = 'index.html'
    queryset = HttpResponse


class ContactList(generic.ListView):
    model = Contact
    queryset = Contact.objects.filter(approved=True).order_by('created_on')
    template_name = 'contact.html'
    paginate_by = 6

    # add contact fom view here

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(approved=True).order_by('created_on')
    template_name = 'booking.html'
    paginate_by = 6

    # add booking form view here
