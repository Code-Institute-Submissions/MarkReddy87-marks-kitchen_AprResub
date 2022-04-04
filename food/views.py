""" relevant imports below """
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Contact
from .forms import ContactForm, BookingForm


class ShowMenu(generic.ListView):
    """ ShowMenu view """
    template_name = 'index.html'
    queryset = HttpResponse


class ShowContacts(generic.ListView):
    """ ShowContact view """
    model = Contact
    queryset = Contact.objects.filter(approved=True).order_by('created_on')
    template_name = 'review.html'
    paginate_by = 6


class ContactList(generic.ListView):
    """ ContactList view """

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'contact.html',
            {
                "contacted": False,
                "contact_form": ContactForm()
            },
        )

    def post(self, request):
        """ Post request function """

        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
        else:
            contact_form = ContactForm()

        return render(
            request,
            'contact.html',
            {
                "contacted": True,
                "contact_form": ContactForm()
            },
        )


class BookingList(generic.ListView):
    """ BookingList view """

    def get(self, request):

        return render(
            request,
            'booking.html',
            {
                "booked": False,
                "booking_form": BookingForm()
            },
        )

    def post(self, request):
        """ Post request function """

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            'booking.html',
            {
                "booked": True,
                "booking_form": BookingForm()
            },
        )
