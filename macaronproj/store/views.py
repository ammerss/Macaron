from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from store.models import Store

#class StoreListView(generic.ListView):
 #   model = Store
    #context_object_name ='store_list'
#가게 목록을 함수로 써도 되는데 리스트로 만드는게 코드도 더 짧고, 반복덜 되고, 관리하기 편함

# Create your views here.
def home(request):
    store_list=Store.objects.all()
    #store_list=StoreListView.as_view()
    return render(request,'home.html',{'store_list':store_list})

def detail(request,pk):
    store=Store.objects.get(pk=pk)
    return render(request,'detail.html',{'store':store})

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