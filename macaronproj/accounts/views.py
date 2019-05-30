from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def update_profile(request, user_id):
    user_data = User.objects.get(pk=user_id)

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user_data = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
            user_data.save()
            if request.POST['type'] == "customer":
                user_data.profile.user_type = False
            else:
                user_data.profile.user_type = True
            user_data.profile.name = request.POST['name']
            user_data.profile.phone = request.POST['tel']
            user_data.profile.email = request.POST['email']
            user_data.save() 
            auth.login(request,user_data)
            return redirect('/')
        else:
            return render(request, 'signup.html')



    else:   
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')

@login_required
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.phone = 1
    user.profile.phone = "0109926420"
    user.save()

@login_required
def editmypage(request, pk):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, pk=pk)
        return render(request, 'editmypage.html', {'profile':profile})
    
    elif request.method == 'PUT':
        profile = get_object_or_404(Profile, pk=pk)
        user = User.objects.get(pk=pk)
        user.profile.phone = 1
        user.profile.phone = "0109926420"
        user.save()
        return redirect('mypage/'+pk)
        # return render(request, 'mypage.html', {'profile':profile})

@login_required
def mypage(request, pk):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, pk=pk)
        return render(request, 'mypage.html', {'profile':profile})
