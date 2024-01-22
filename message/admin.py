from django.contrib import admin
from message.models import Message, Chat, Badword

admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Badword)
