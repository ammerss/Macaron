from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from store.models import Store

# Create your views here.
def home(request):
    store_list=Store.objects.all()
    return render(request,'home.html',{'store_list':store_list})

def detail(request,pk):
    store=Store.objects.get(pk=pk)
    return render(request,'detail.html',{'store':store})

def edit(request):
    return render(request,'edit.html')   

def new(request):
    return render(request,'new.html')

def create_store(request):
    store=Store()
    store.name=request.POST['name']
    store.num=request.POST['number']
    store.content=request.POST['body']
    store.save()

    return redirect ('/store')