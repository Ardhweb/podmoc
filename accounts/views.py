from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import LoginForm,SignupForm
from .models import User
from django.db.models import Q 

def register_student_user(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.user_role == User.UserRole.STUDENT
            try:
                new_user.save()
            except Exception as e:
                return HttpResponse(f"Student User Creation Issue: {e}")
            user = authenticate(request,  username_or_email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("User not Exist!")   
    else:
        user_form = SignupForm()
    return render(request,'accounts/register_student.html',{'user_form': user_form})


def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username_or_email=cd['username_or_email'], password=cd['password'])
            print(f"Authenticated user: {user}")  # Debug statement
            if user is not None and user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Authentication failed: User not found or inactive")
        else:
            return HttpResponse("Form is invalid")
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

def logout_user(request):
    logout(request)  # Log the user out
    return redirect('index')


def register_teacher_user(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.user_role == User.UserRole.TEACHER
            try:
                new_user.save()
            except Exception as e:
                return HttpResponse(f"Teacher User Creation Issue: {e}")
            user = authenticate(request,  username_or_email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("User not Exist!")   
    else:
        user_form = SignupForm()
    return render(request,'accounts/register_teacher.html',{'user_form': user_form})
