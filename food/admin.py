from django.contrib import admin
from .models import Booking, Contact


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('party_name', 'booking_date', 'approved', 'created_on')
    search_fields = ['party_name', 'phone', 'booking_date']
    list_filter = ('approved', 'created_on')
    actioins = ['approved_bookings']

    def approved_bookings(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('title', 'name', 'created_on')
    search_fields = ['name', 'email', 'title']
    list_filter = ('email', 'name')
