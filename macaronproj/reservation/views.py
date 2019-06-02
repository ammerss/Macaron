from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Reservation
from store.models import Store, Macarons
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

def Reser_owner(request):
    return render(request, 'list.html')

def Reser_custom(request):
    return render(request, 'cart.html')

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
        reser = Reservation()
        reser.reser_num = reser_request_time.strftime('%Y%m%d') + str(shop_name.id).zfill(4) + "_" + str(count).zfill(3)
        count += 1
        if(count>999): count = 0
        reser.customer = customer
        reser.shop_name = shop_name
        reser.quantity = quantity
        reser.choice_macaron = macaron
        reser.reser_request_time = reser_request_time
        reser.reser_time = reser_time
        reser.save()
        messages.success(request, 'Reservation success!')
        return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))

    return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))