from django.shortcuts import render
#from . import Store

# Create your views here.
def home(request):
    # store_list=Store.objects.all()
    # return render(request,'home.html',{'store_list':store_list})
    return render(request,'home.html')