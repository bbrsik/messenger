from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from message.models import Message
import json


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
    if request.method == "POST":
        body = json.loads(request.body)
        text = body.get('message')
        msg = Message(text=text, user=request.user)
        msg.save()
    return HttpResponse()
