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
        return 0  # something that refuses to continue the profile edit procedure

    return 0


@csrf_exempt
def create_user(request):
    username = request.POST.get('username')
    if User.objects.filter(username=username).exists():
        request.session['signup_failed'] = True
        return redirect('/user/signup/')
    password = request.POST.get('password')
    User.objects.create_user(
        username=username, email=None, password=password
    )
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return redirect('/message/chats/')
