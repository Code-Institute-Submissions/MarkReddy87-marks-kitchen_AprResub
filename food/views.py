from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.views import generic, View
from .models import Contact, Booking
from .forms import ContactForm, BookingForm


class ShowMenu(generic.ListView):
    template_name = 'index.html'
    queryset = HttpResponse


class ShowContacts(generic.ListView):
    model = Contact
    queryset = Contact.objects.filter(approved=True).order_by('created_on')
    template_name = 'review.html'
    paginate_by = 9


class ContactList(generic.ListView):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'contact.html',
            {
                "contact_form": ContactForm()
            },
        )


# class BookingList(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.filter(approved=True).order_by('created_on')
#     template_name = 'booking.html'
#     paginate_by = 6


class BookingList(generic.ListView):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'booking.html',
            {
                "booking_form": BookingForm()
            },
        )
        
