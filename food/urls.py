from . import views
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.ShowMenu.as_view(), name='menu'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
