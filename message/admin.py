from django.contrib import admin
from message.models import Message, Chat
from weather.models import Weather

admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Weather)
