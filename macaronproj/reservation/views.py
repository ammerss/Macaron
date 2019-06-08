from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from reservation.models import Reservation
from store.models import Store, Macarons
from accounts.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

def reserve(request, pk):
    store = get_object_or_404(Store, pk=pk)
    product_list = store.macarons_set.all()
    return render(request, 'show.html', {'product_list': product_list, 'store': store})

count = 0

@login_required
def request_reservation(request, pk):
    global count
    customer = request.user
    shop_name = get_object_or_404(Store, pk=pk)

    macaron_name = request.POST.get('choice')
    if not macaron_name:
        messages.error(request, 'ERROR: Please choice MACARON TYPE!')
        return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))
    
    quantity = int(request.POST.get(macaron_name))
    if quantity == 0:
        messages.error(request, 'ERROR: Please fill the form of COUNT')
        return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))

    reser_request_time = timezone.datetime.now()
    #convert date value and time value to Datetime form
    if(request.POST.get('date')=='' or request.POST.get('time')==''):
        messages.error(request, 'ERROR: Please fill the form of DATE and TIME')
        return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))

    date = datetime.datetime.strptime(request.POST.get('date'), "%Y-%m-%d").date()
    time = datetime.datetime.strptime(request.POST.get('time'), "%H:%M").time()
    reser_time = datetime.datetime.combine(date, time)

    if request.method == 'POST':
        reservation = Reservation()
        count += 1
        reservation.reser_num = count
        reservation.customer = customer
        reservation.shop_name = shop_name
        reservation.quantity = quantity
        macaron_list = shop_name.macarons_set.all()
        for macaron in macaron_list:
            if macaron.name == macaron_name:
                price = macaron.price
                if quantity > macaron.stock:
                    messages.error(request, "ERROR: You can only reserve less than left macaron")
                    return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))
                macaron.stock -= quantity
                macaron.save()
                break
        reservation.amount = int(quantity*price)
        reservation.choice_macaron = macaron_name
        reservation.reser_request_time = reser_request_time
        reservation.reser_time = reser_time
        reservation.save()
        messages.success(request, 'Reservation success!')
        return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))
    return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))

def Reser_owner(request, pk):
    store = get_object_or_404(Store, pk=pk)
    reservation_list = store.reservation_set.all()                                       
    return render(request, 'reservations.html', { 'store' : store,'reservation_list': reservation_list})

def Reser_list_owner(request,pk):
    profile = get_object_or_404(Profile, pk=pk)
    store_list = Store.objects.all().filter(owner=profile.user)  
    return render(request, 'list.html', {'profile':profile, 'store_list' : store_list})

def Reser_custom(request,pk):
    customer = get_object_or_404(User, pk=pk)
    reservation_list = customer.reservation_set.all()
    return render(request, 'cart.html', {'reservation_list': reservation_list, 'customer': customer})

def approve(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        if request.POST['type'] == "approve":
            reservation.approve = 1
            reservation.save()
        else:
            reservation.approve = 2
            reservation.save()
            store=reservation.shop_name
            macaron_list = Macarons.objects.all().filter(store=store)
            for macaron in macaron_list:
                if macaron.name==reservation.choice_macaron:
                    macaron.stock += reservation.quantity
                    macaron.save()
                    break
        return render(request, 'approve.html', {'reservation': reservation} )                
    return render(request, 'approve.html', {'reservation': reservation})
   