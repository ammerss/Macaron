from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from .models import Reservation
from store.models import Store, Macarons
from django.http import HttpResponseRedirect
from django.contrib import messages

def Reser_owner(request):
    return render(request, 'list.html')

def Reser_custom(request):
    return render(request, 'cart.html')

def reserve(request, pk):
    store = get_object_or_404(Store, pk=pk)
    product_list = store.macarons_set.all()
    return render(request, 'show.html', {'product_list': product_list, 'store': store})


def request_reservation(request, pk):

    store = get_object_or_404(Store, pk=pk)
    #customer = request.user
    quantity = request.POST.get('number')
    shop_name = store
    macaron = request.POST.get('macaron')
    reser_request_time = timezone.datetime.now()
    reser_time = request.POST.get('date') + request.POST.get('time')

    if request.method == 'POST':
        reser = Reservation()
        #reser.customer = customer
        reser.shop_name = shop_name
        reser.quantity = quantity
        reser.choice_macaron = macaron
        reser.reser_request_time = reser_request_time
        reser.reser_time = reser_time
        reser.save()
        messages.success(request, 'Reservation success!')
        return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))

    return HttpResponseRedirect(reverse('reservation:reserve', args=(pk,)))