from django.shortcuts import render, redirect
from django.utils import timezone
from store.models import Store


# Create your views here.
def home(request):
    store_list=Store.objects
    return render(request,'home.html',{'store_list':store_list})

def detail(request):
    return render(request,'detail.html')

def edit(request):
    return render(request,'edit.html')   

def new(request):
    return render(request,'new.html')

def create(request):
    store=Store()
    store.name=request.POST['name']
    store.num=request.POST['number']
    store.content=request.POST['body']
    store.save()

    return redirect ('/store')