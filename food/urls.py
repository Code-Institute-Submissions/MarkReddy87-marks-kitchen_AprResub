from . import views
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.ShowMenu.as_view(), name='menu'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('contact.html', views.ContactList.as_view(), name='contact'),
    path('booking.html', views.BookingList.as_view(), name='booking'),
    path('review.html', views.ShowContacts.as_view(), name='review'),
]
