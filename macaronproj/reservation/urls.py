from django.contrib import admin
from django.urls import path
import reservation.views

app_name="reservation"
urlpatterns = [
    path('reservate',reservation.views.reservate, name='reservate'),
]