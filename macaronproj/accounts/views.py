from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
<<<<<<< HEAD
from .forms import SignupForm
=======
from .models import Profile
from django.contrib.auth.decorators import login_required
>>>>>>> 00a29c4fff0b54a9642fc91360022187a7c3db3d

def signup(request):
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()
            return redirect('home')
    else:
        signupform = SignupForm()
        return render(request, 'signup.html', {'signupform':signupform})

    # if request.method == 'POST':
    #     if request.POST['password1'] == request.POST['password2']:
    #         #아이디가 같은 경우
    #         try:
    #             user = User.objects.get(username=request.POST['username'])
    #             return render(request, 'signup.html', {'error': 'Username has already been taken'})
    #         except User.DoesNotExist:
    #             user = User.objects.create_user(
    #                 request.POST['username'], password=request.POST['password1'])
    #             auth.login(request, user)
    #             return redirect('home')
    #     else:
    #         return render(request, 'signup.html', {'error': 'Passwords must match'})
    # else:
    #     return render(request, 'signup.html')

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
<<<<<<< HEAD
=======

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
>>>>>>> 00a29c4fff0b54a9642fc91360022187a7c3db3d
