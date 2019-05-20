from django.shortcuts import render
from .models import reservation

def Reser_owner(request):
    return render(request, 'list.html')

def Reser_custom(request):
    return render(request, 'cart.html')

def reservate(request):
    return render(request, 'show.html')


def request_reservation(request):

    customer = request.user
    quantity = int(request.POST.get('quantity'))
    shop_name = request.shop_name
    product = Product.objects.get()
    reser_request_time = request.time
    reser_time = timezone.datetime.now()

    if request.method == 'POST':
        if 'reservate' in request.POST:
            reser = Reservation()
            reser.customer = customer
            reser.shop_name = shop_name
            reser.quantity = quantity
            reser.product = product
            reser.reser_request_time = reser_request_time
            reser.reser_time = reser_time