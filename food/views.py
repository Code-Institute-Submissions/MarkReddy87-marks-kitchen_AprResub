from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import generic, View
from .models import Contact


class ShowMenu(generic.ListView):
    template_name = 'index.html'
    queryset = HttpResponse


class ContactList(generic.ListView):
    model = Contact
    queryset = Contact.objects.order_by('created_on')
    template_name = 'contact.html'
    paginate_by = 6
