import urllib
import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from message.serializers import *


@csrf_exempt
def login_view(request):
    body = json.loads(request.body)
    user = authenticate(request, username=body.get('username'), password=body.get('password'))
    if not user:
        return JsonResponse({}, status=403)
    login(request, user=user)
    return JsonResponse({})


@csrf_exempt
def create_message(request, chat_id):
    if request.method != "POST":
        return JsonResponse({}, status=400)
    ## todo анонимный пользователь - исключение
    body = urllib.parse.parse_qs(request.body.decode())
    [message] = body.get('message')
    chat = chat_id
    try:
        Chat.objects.get(id=chat)
    except Chat.DoesNotExist:
        return JsonResponse({'Chat does not exist.'}, status=400)

    msg = Message(text=message, user=request.user, chat_id=chat)
    msg.save()
    return redirect(reverse("render_chat", kwargs={'chat_id': chat_id}))


@csrf_exempt
def delete_message(request, message_id):
    if request.method != "POST":
        return JsonResponse({}, status=400)
    try:
        message = Message.objects.get(id=message_id)
        chat_id = message.chat.id
        message.delete()
        return redirect(reverse("render_chat", kwargs={'chat_id': chat_id}))
    except Message.DoesNotExist:
        return JsonResponse({'Message does not exist'}, status=400)


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        body = urllib.parse.parse_qs(request.body.decode())
        [name] = body.get('name')
        chat = Chat(name=name)
        chat.save()
    return redirect(reverse("render_list"))


def show_chat(request, chat_id):
    if request.method != "GET":
        return JsonResponse({}, status=400)

    try:
        Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return JsonResponse({'Response': 'Chat does not exist'}, status=404)
    messages = serialize_messages(Message.objects.filter(chat_id=chat_id))
    return JsonResponse({'messages': messages})


def list_chats(request):
    if request.method != "GET":
        return JsonResponse({}, status=400)
    chats = serialize_chats(Chat.objects.all())
    return JsonResponse({'chats': chats})
