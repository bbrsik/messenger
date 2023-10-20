from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"NAME: {self.name}, "
            f"ID: {self.id}"
        )


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply_on = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def get_replies_chain(self):
        current = self.reply_on
        reply_array = []
        while current is not None:
            reply_array.append(current)
            current = current.reply_on
        return reply_array

    def __str__(self):
        return (
            f"CHAT: {self.chat}; "
            f"USER: {self.user}; "
            f"DATE: ({self.created_at:%Y-%m-%d %H:%M}): "
            f"MESSAGE: {self.text}"
        )


