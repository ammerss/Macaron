from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

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

@login_required
def editmypage(request, pk):
    if request.method == 'POST':
        if request.POST['passwd'] == request.POST['repasswd']:
            user = User.objects.get(username=request.POST['username'])
            if request.POST['type'] == "customer":
                user.profile.user_type = False
            else:
                user.profile.user_type = True
            user.password = request.POST['passwd']
            user.profile.name = request.POST['name']
            user.profile.phone = request.POST['phone']
            user.save()
            return redirect('/')
        else:
            return render(request, 'signup.html')
    else:
        profile = get_object_or_404(Profile, pk=pk)
        return render(request, 'editmypage.html', {'profile':profile})

@login_required
def mypage(request, pk):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, pk=pk)
        return render(request, 'mypage.html', {'profile':profile})

@csrf_exempt
def contact(request):
    return HttpResponse('Hello world')