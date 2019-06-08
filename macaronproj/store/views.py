from django.shortcuts import render, redirect,get_object_or_404,reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from store.models import Store, Macarons
from .forms import PhotoForm,ImageForm
from accounts.models import Profile
from django.contrib import messages


# Create your views here.
def home(request):
    store_list=Store.objects.all()
    #return render(request,'home.html',{'store_list':store_list})

    if 'search' in request.GET:
        query = request.GET['search']  
        stores = Store.objects.all().filter(name__contains=query)
        result = stores    
        return render(request, 'home.html', {'searched_stores' : result, 'query': query })    
    else:
        result = None
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
           return HttpResponseRedirect(reverse('store:detail', kwargs={'pk': pk}))

    else:
        form=PhotoForm()
        return render(request,'edit.html',{'store':store,'form':form})   

def new(request):
        form=ImageForm()
        return render(request,'new.html',{'form':form})

def create_store(request):
    if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                    info = form.save(commit=False)
                    info.name = request.POST.get('name', '')
                    info.num = request.POST.get('number', '')
                    info.content = request.POST.get('body', '')
                    info.owner = request.user
                    
                    info.save()
                    return redirect('/store')
            

   

def mystores(request, user_id):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, pk=user_id)
        stores = Store.objects.all().filter(owner=profile.user)
    
    return render(request, 'mystores.html', {'profile':profile, 'store_list' : stores})
    
    

def editmystore(request, user_id , store_id):
     if request.method == 'POST':
        store=Store.objects.get(pk=store_id)
        store.name = request.POST['storename']
        store.num = request.POST['storenumber']
        store.content = request.POST['storecontent']
        store.save()
        profile = get_object_or_404(Profile, pk=user_id)
        stores = Store.objects.all().filter(owner=profile.user)
        return render(request,'mystores.html', {'profile':profile,'store_list' : stores})

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
        

