from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from message.models import Message


# Create your views here.


def list_messages(request):
    messages = []
    for msg in Message.objects.all():
        messages.append({
            'created_at': msg.created_at.strftime("%D %H:%M:%S"),
            'username': msg.user.username,
            'user_id': msg.user_id,
            'text': msg.text
        })
    print(request.method)
    return HttpResponse(messages)


@csrf_exempt
def create_message(request):
    if request.method == "POST":
        print(request.POST)
    return HttpResponse()
