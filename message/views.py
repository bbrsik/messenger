from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from message.models import Message
from message.models import Chat
import json
from django.views.decorators.http import require_http_methods


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
    c = body.get('chat')
    try:
        Chat.objects.get(id=c)
    except Chat.DoesNotExist:
        return JsonResponse({'Chat does not exist.'}, status=400)

    msg = Message(text=text, user=request.user, chat_id=c)
    msg.save()
    return JsonResponse({})


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        body = json.loads(request.body)
        text = body.get('name')
        n = Chat(name=text)
        n.save()
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

    return JsonResponse({'messages': messages})


def list_chats(request):
    if request.method != "GET":
        return JsonResponse({}, status=400)

    chats = []
    for c in Chat.objects.all():
        chats.append({
            'created_at': c.created_at.strftime("%D %H:%M:%S"),
            'id': c.id,
            'name': c.name
        })

    return JsonResponse({'chats': chats})
