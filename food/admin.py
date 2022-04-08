""" Revevant Imports below for admin page """
from django.contrib import admin
from .models import Booking, Contact


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Setting up booking admin panel """

    list_display = ('party_name', 'booking_date', 'approved', 'created_on')
    search_fields = ['party_name', 'phone', 'booking_date']
    list_filter = ('approved', 'created_on')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        """ Setting queryset for approved checkbox """
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Setting up contact admin panel """

    prepopulated_fields = {'slug': ('title',)}

    list_display = ('title', 'name', 'approved', 'slug', 'created_on')
    search_fields = ['name', 'email', 'title']
    list_filter = ('email', 'name', 'created_on')
    actions = ['approve_contacts']

    def approve_contacts(self, request, queryset):
        """ Setting queryset for approved checkbox """
        queryset.update(approved=True)
