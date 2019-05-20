from django.contrib import admin
from django.urls import path
import reservation.views

app_name="reservation"
urlpatterns = [
    path('Reser_owner',reservation.views.Reser_owner, name='Reser_owner'),
    path('Reser_custom', reservation.views.Reser_custom, name ='Reser_custom'),
    path('reservate',reservation.views.reservate, name='reservate'),
]