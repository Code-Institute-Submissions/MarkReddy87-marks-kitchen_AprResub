""" Revevant Imports below for admin page """
from django.contrib import admin
from .models import Booking, Contact


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Setting up booking admin panel """

    list_display = ('party_name', 'booking_date', 'approved', 'created_on')
    search_fields = ['party_name', 'phone', 'booking_date']
    list_filter = ('approved', 'created_on')
    actioins = ['approve_bookings']

    def approved_bookings(self, request, queryset):
        """ Setting queryset for approved checkbox """
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Setting up contact admin panel """

    list_display = ('title', 'name', 'approved', 'created_on')
    search_fields = ['name', 'email', 'title']
    list_filter = ('email', 'name', 'created_on')

    def approved_contact(self, request, queryset):
        """ Setting queryset for approved checkbox """
        queryset.update(approved=True)
