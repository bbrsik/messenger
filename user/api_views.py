import urllib
import django.contrib.auth.hashers
from user.models import Profile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/message/chats/')
    else:
        request.session['login_failed'] = True
        return redirect('/user/login/')


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('/user/login/')


@csrf_exempt
def edit_profile(request):
    user = request.user

    if not user.is_authenticated:
        # something that refuses to continue the profile edit procedure

        return redirect('/user/profile/')

    if not user.check_password(request.POST.get('password')):
        # send a message that the password is wrong

        request.session['edit_failed'] = True
        return redirect('/user/profile/')

    profile = Profile.objects.get(user=request.user)
    profile.first_name = request.POST.get('first_name')
    profile.last_name = request.POST.get('last_name')
    profile.middle_name = request.POST.get('middle_name')
    profile.current_location = request.POST.get('current_location')
    profile.birthdate = request.POST.get('birthdate')

    picture = request.FILES.get('picture')
    if picture:
        profile.picture = picture

    profile.save()
    request.session['edit_succeeded'] = True
    return redirect('/user/profile/')


@csrf_exempt
def create_user(request):
    username = request.POST.get('username')
    if User.objects.filter(username=username).exists():
        request.session['signup_failed'] = True
        return redirect('/user/signup/')
    password = request.POST.get('password')
    new_user = User.objects.create_user(
        username=username, email=None, password=password
    )
    user = authenticate(request, username=username, password=password)
    profile = Profile.objects.create(user=new_user)
    login(request, user=new_user)
    return redirect('/message/chats/')
