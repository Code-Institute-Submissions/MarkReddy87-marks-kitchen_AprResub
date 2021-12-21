from . import views
from django.urls import path


urlpatterns = [
    path('', views.ShowMenu.as_view(), name='menu')
]
