from django.contrib import admin
from django.urls import path
import reservation.views

app_name="reservation"
urlpatterns = [
    path('Reser_owner/<int:s_id>>',reservation.views.Reser_owner, name='Reser_owner'),
    path('Reser_list_owner/<int:pk>',reservation.views.Reser_list_owner, name='Reser_list_owner'),
    path('Reser_custom/<int:pk>', reservation.views.Reser_custom, name ='Reser_custom'),
    path('reserve/<int:pk>',reservation.views.reserve, name='reserve'),
    path('reserve/<int:pk>/request_reservation/', reservation.views.request_reservation, name='request_reservation'),
    path('Reser_owner/<int:pk>/request_approve/', reservation.views.request_approve, name='request_approve'),
    path('Reser_owner/<int:pk>/request_reject/', reservation.views.request_approve, name='request_reject'),
]