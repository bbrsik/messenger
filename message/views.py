from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from message.models import Message
from message.models import Chat
import json


def render_chat(request, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return JsonResponse({'Response': 'Chat does not exist'}, status=404)

    messages = show_chat(request, chat_id)
    context = {
        'chat_id': chat_id,
        'name': chat.name,
        'messages': messages,
    }
    return render(request, 'render_chat.html', context=context)


@csrf_exempt
def login_view(request):
    body = json.loads(request.body)
    user = authenticate(request, username=body.get('username'), password=body.get('password'))
    if not user:
        return JsonResponse({}, status=403)
    login(request, user=user)
    return JsonResponse({})


@csrf_exempt
def create_message(request):
    if request.method != "POST":
        return JsonResponse({}, status=400)

    body = json.loads(request.body)
    text = body.get('message')
    chat = body.get('chat_id')
    try:
        Chat.objects.get(id=chat)
    except Chat.DoesNotExist:
        return JsonResponse({'Chat does not exist.'}, status=400)

    msg = Message(text=text, user=request.user, chat_id=chat)
    msg.save()
    return JsonResponse({})


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        body = json.loads(request.body)
        text = body.get('name')
        chat = Chat(name=text)
        chat.save()
    return JsonResponse({})


def show_chat(request, chat_id):
    if request.method != "GET":
        return JsonResponse({}, status=400)

    try:
        Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return JsonResponse({'Response': 'Chat does not exist'}, status=404)

    messages = []
    for msg in Message.objects.filter(chat_id=chat_id):
        messages.append({
            'created_at': msg.created_at.strftime("%D %H:%M:%S"),
            'username': msg.user.username,
            'text': msg.text,
            'id': msg.id,
        })

    return messages
    # return JsonResponse({'messages': messages})



def list_chats(request):
    if request.method != "GET":
        return JsonResponse({}, status=400)

    chats = []
    for chat in Chat.objects.all():
        chats.append({
            'created_at': chat.created_at.strftime("%D %H:%M:%S"),
            'id': chat.id,
            'name': chat.name
        })

    return render(request, 'render_list.html', context=chat_names)
