from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            #아이디가 같은 경우
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
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
    return render(request, 'signup.html')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.phone = 1
    user.profile.phone = "0109926420"
    user.save()

def edit(request):
    if request.method == 'PUT':
        profiles = Profile.objects
    return render(request, 'edit.html', {'profile':profiles})

def mypage(request):
    if request.method == 'GET':
        profiles = Profile.objects
    return render(request, 'mypage.html', {'profile':profiles})