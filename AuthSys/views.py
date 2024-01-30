from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import Signup
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Signup(request.POST)
            if form.is_valid():
                form.save()
                # update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/profile/')
        else:
            form = Signup()  # Define the form in the else block
        context = {'form': form}    
        return render(request, 'signup.html', context)
    return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user.username})
    else:
        return HttpResponseRedirect('/login/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    return HttpResponseRedirect('/profile/')



def user_logout(request):
    logout(request)
    return redirect('login')


# Change password with old password
def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'changePass.html',{'form': form})
    return HttpResponseRedirect('/login/')



# Change Password without old password
def user_change_password_wo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'changePass2.html',{'form': form})
    return HttpResponseRedirect('/login/')



def home(request):
    return render(request, 'home.html', {})