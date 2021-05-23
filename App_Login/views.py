from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def sign_up(request):
    form = forms.SignUpForm()
    registered = False

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            registered = True
        
    diction = {
        'form': form,
        'registered': registered,
    }

    return render(request, 'App_Login/sign_up.html', context=diction)

def login_page(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)

                return redirect('index')


    diction = {
        'form': form,
    }    

    return render(request, 'App_Login/login.html', context = diction)

@login_required
def logout_user(request):
    logout(request)

    return redirect('App_Login:login')   

@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={})    

@login_required
def update_profile(request):
    form = forms.UserProfileChange(instance = request.user)

    if request.method == 'POST':
        form = forms.UserProfileChange(request.POST, instance = request.user)

        if form.is_valid():
            form.save(commit=True)

            return redirect('App_Login:profile')
    diction = {
        'form': form,
    }     

    return render(request, 'App_Login/update_profile.html', context=diction)

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    changed = False

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)

        if form.is_valid():
            form.save()
            changed =True
            
    diction = {
        'form': form,
        'changed': changed,
    }    

    return render(request, 'App_Login/change_password.html', context=diction)

@login_required
def add_profile_pic(request):
    form = forms.ProfilePic()

    if request.method == 'POST':
        form = forms.ProfilePic(request.POST, request.FILES)

        if form.is_valid():
            user_prof = form.save(commit=False)
            user_prof.user = request.user

            user_prof.save()

            return redirect('App_Login:profile')
    diction = {
        'form': form
    }

    return render(request, 'App_Login/add_profile_pic.html', context = diction)

@login_required
def change_profile_pic(request):
    form = forms.ProfilePic(instance=request.user.user_profile)

    if request.method == 'POST':
        form = forms.ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)

        if form.is_valid():
            form.save(commit=True)

            return redirect('App_Login:profile')
    diction = {
        'form': form,
    }

    return render(request, 'App_Login/change_profile_pic.html', context=diction)