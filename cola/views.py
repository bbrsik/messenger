from django.shortcuts import redirect


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect('/message/chats/')
    else:
        return redirect('/user/login/')
