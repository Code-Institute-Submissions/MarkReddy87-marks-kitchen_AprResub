""" relevant imports below """
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
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


class ReviewDetail(View):
    """ ReviewDetail view """
    def get(self, request, slug):
        """ function to get specific review """
        queryset = Contact.objects.filter(approved=True)
        review = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
            },
        )


class DeleteContact(DeleteView):
    """ Delete a Review view """
    model = Contact
    success_url = reverse_lazy('review')


class EditContact(View):
    """ EditContact View """
    def get(self, request, slug):
        """ Get instance of Contactform """
        review = get_object_or_404(Contact, slug=slug)
        form = ContactForm(instance=review)

        return render(
            request,
            "edit_contact.html",
            {
                "form": form,
                "contacted": False,
            },
        )

    def post(self, request, slug):
        """ Post request function """
        review = get_object_or_404(Contact, slug=slug)
        contact_form = ContactForm(data=request.POST, instance=review)

        if contact_form.is_valid():
            contact_form.save()
        else:
            contact_form = ContactForm()

        return render(
            request,
            'contact.html',
            {
                "contacted": True,
                "contact_form": contact_form,
            },
        )


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
            contact_form.instance.name = request.user
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
    def get(self, request, *args, **kwargs):

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
            booking_form.instance.user_name = request.user
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
