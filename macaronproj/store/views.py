from django.shortcuts import render, redirect,get_object_or_404,reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from store.models import Store, Macarons
from .forms import PhotoForm

# Create your views here.
def home(request):
    store_list=Store.objects.all()
    return render(request,'home.html',{'store_list':store_list})

def detail(request,pk):
    store=get_object_or_404(Store, pk=pk)
    product_list = store.macarons_set.all()
    #product_list = Macarons.objects.filter(store=store.name)
    return render(request,'detail.html',{'product_list':product_list,'store':store})

def edit(request,pk):
    store = get_object_or_404(Store,pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
           content= form.save(commit=False)
           name = request.POST.get('title','')
           price = request.POST.get('cost','')
           stock = request.POST.get('num','')
           
           content.name=name
           content.price=price
           content.stock=stock
           content.store=store
        #    content = Macarons(id=None, name=name, price=price, stock=stock ,store=store)
           content.save()
       
           return render(request,'detail.html', args=(pk,))
    else:
        form=PhotoForm()
        return render(request,'edit.html',{'store':store,'form':form})   

def new(request):
    return render(request,'new.html')

def create_store(request):
    store=Store()
    store.name=request.POST['name']
    store.num=request.POST['number']
    store.content=request.POST['body']
    store.save()

    return redirect ('/store')

# def upload_pic(request,pk):
#     #content = get_object_or_404(Macarons, pk=pk)
#     store = get_object_or_404(Store, pk=pk)

    
#     name = request.POST.get('title','')
#     price = request.POST.get('cost','')
#     stock = request.POST.get('num','')
   
#     if request.method == 'POST':
#        # form = PhotoForm(request.POST.get('picture',''))
#         form = PhotoForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save(commit=False)   
#             content = Macarons(id=None, name=name, price=price, stock=stock ,store=store)
#             content.save()
#         return HttpResponseRedirect(reverse('store:edit', args=(pk,)))
        