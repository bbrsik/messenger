from django.contrib.auth import authenticate, login
from django.http import HttpResponse
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
        return HttpResponse(status=403)
    login(request, user=user)
    return HttpResponse()


def list_messages(request):
    messages = []
    for msg in Message.objects.all():
        messages.append({
            'created_at': msg.created_at.strftime("%D %H:%M:%S"),
            'username': msg.user.username,
            'user_id': msg.user_id,
            'text': msg.text
        })
    return HttpResponse(messages)


@csrf_exempt
def create_message(request):
    if request.method != "POST":
        return HttpResponse(status=400)

    body = json.loads(request.body)
    text = body.get('message')
    c = body.get('chat')
    try:
        Chat.objects.get(id=c)
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist.', status=400)

    msg = Message(text=text, user=request.user, chat_id=c)
    msg.save()
    return HttpResponse()


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        body = json.loads(request.body)
        text = body.get('name')
        n = Chat(name=text)
        n.save()
    return HttpResponse()


# def list_chats(request):
#     chats = []
#     for c in Chat.objects.all():
#         chats.append({
#             'created_at': c.created_at.strftime("%D %H:%M:%S"),
#             'name': c.user.username,
#             'text': c.text
#         })
#     return HttpResponse(chats)
