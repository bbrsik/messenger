from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User


@csrf_exempt
def render_login(request):
    if request.user.is_authenticated:
        return redirect('/message/chats/')
    login_failed = request.session.get('login_failed', False)
    if login_failed:
        messages.error(request, 'Wrong username or password')
        del request.session['login_failed']
    return render(request, 'render_login.html', {'login_failed': login_failed})


@csrf_exempt
def render_signup(request):
    if request.user.is_authenticated:
        return redirect('/message/chats/')
    signup_failed = request.session.get('signup_failed', False)
    if signup_failed:
        messages.error(request, 'User already exists')
        del request.session['signup_failed']
    return render(request, 'render_signup.html', {'signup_failed': signup_failed})


def render_profile(request):
    if not request.user.is_authenticated:
        return redirect('/user/login/')
    return render(request, 'render_profile.html')

