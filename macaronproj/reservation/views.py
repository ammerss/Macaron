from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from reservation.models import Reservation
from store.models import Store, Macarons
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

def reserve(request, pk):
    store = get_object_or_404(Store, pk=pk)
    product_list = store.macarons_set.all()
    return render(request, 'show.html', {'product_list': product_list, 'store': store})

@login_required
def request_reservation(request, pk):
    count = 1
    customer = request.user
    shop_name = get_object_or_404(Store, pk=pk)
    quantity = request.POST.get('quantity')
    macaron = ''
    reser_request_time = timezone.datetime.now()
    #convert date value and time value to Datetime form
    date = datetime.datetime.strptime(request.POST.get('date'), "%Y-%m-%d").date()
    time = datetime.datetime.strptime(request.POST.get('time'), "%H:%M").time()
    reser_time = datetime.datetime.combine(date, time)

    if request.method == 'POST':
        reservation = Reservation()
        reservation.reser_num = reser_request_time.strftime('%Y%m%d') + str(shop_name.id).zfill(4) + str(count).zfill(3)
        count += 1
        if(count>999): count = 0
        reservation.customer = customer
        reservation.shop_name = shop_name
        reservation.quantity = quantity
        reservation.choice_macaron = macaron
        reservation.reser_request_time = reser_request_time
        reservation.reser_time = reser_time
        reservation.save()
        messages.success(request, 'Reservation success!')
        return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))
    return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))

def Reser_owner(request,pk):
    store = get_object_or_404(Store, pk=pk)
    shop_name = store
    reservation_list = shop_name.reservation_set.all()
    return render(request, 'list.html', {'reservation_list': reservation_list, 'shop_name': shop_name})

def Reser_custom(request,pk):
    customer = get_object_or_404(User, pk=pk)
    reservation_list = customer.reservation_set.all()
    return render(request, 'cart.html', {'reservation_list': reservation_list, 'customer': customer})

def request_approve(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.approve = 1
        reservation.save()
        pk=reservation.shop_name.id
        return HttpResponseRedirect(reverse('reservation:Reser_owner', args=(pk,)))
    return HttpResponseRedirect(reverse('reservation:Reser_owner', args=(pk,)))    
        

 