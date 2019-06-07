from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

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
def editmypage(request, pk):
    if request.method == 'POST':
        if len(request.POST['passwd']) <= 0 or len(request.POST['repasswd']) <= 0 or len(request.POST['name']) <= 0 or len(request.POST['phone']) <= 0:
            messages.success(request, 'Fill in the all blanks.')
            return HttpResponseRedirect(reverse('accounts:editmypage', args=(pk,)))
        else:
            if request.POST['passwd'] == request.POST['repasswd']:
                user = User.objects.get(id=pk)
                if request.POST['type'] == "customer":
                    user.profile.user_type = False
                else:
                    user.profile.user_type = True
                user.set_password(request.POST['passwd'])
                user.profile.name = request.POST['name']
                user.profile.phone = request.POST['phone']
                user.save()
                return redirect('/')
            else:
                messages.success(request, 'Please re-confirm your password.')
                return HttpResponseRedirect(reverse('accounts:editmypage', args=(pk,)))
    else:
        profile = get_object_or_404(Profile, pk=pk)
        return render(request, 'editmypage.html', {'profile':profile})

@login_required
def mypage(request, user_id):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, pk=user_id)
        return render(request, 'mypage.html', {'profile':profile})
