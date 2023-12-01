import urllib
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, AnonymousUser
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from message.serializers import *


@csrf_exempt
def create_message(request, chat_id):
    if request.method != "POST":
        return JsonResponse({}, status=400)
    body = urllib.parse.parse_qs(request.body.decode())
    [message] = body.get('message')
    if not message:
        return JsonResponse({'message': 'Field "message" is required.'}, status=403)
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
