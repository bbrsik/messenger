from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from message.serializers import *


def render_chat(request, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return JsonResponse({'Response': 'Chat does not exist'}, status=404)
    messages = serialize_messages(Message.objects.filter(chat_id=chat_id))
    chat_has_messages = bool(len(messages))
    context = {
        'chat_id': chat_id,
        'name': chat.name,
        'messages': messages,
        'chat_has_messages': chat_has_messages,
    }
    return render(request, 'render_chat.html', context=context)


def render_list(request):
    chats = serialize_chats(Chat.objects.all())
    context = {
        'chats': chats,
    }
    return render(request, 'render_list.html', context=context)


@csrf_exempt
def render_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if not user:
        return render(request, 'render_login.html')

    login(request, user)
    return redirect('/message/chats/')


@csrf_exempt
def render_signup(request):
    return render(request, 'render_signup.html')