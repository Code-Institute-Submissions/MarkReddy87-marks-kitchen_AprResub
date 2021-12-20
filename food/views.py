from django.shortcuts import render
from django.views import generic
from .models import Contact

class ContactList(generic.ListView):
    model = Contact
    queryset = Contact.objects.order_by('created_on')
    template_name = 'contact.html'
    paginate_by = 5

