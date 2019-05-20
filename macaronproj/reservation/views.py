from django.shortcuts import render
from .models import reservation

def Reser_owner(request):
    return render(request, 'list.html')

def Reser_custom(request):
    return render(request, 'cart.html')
