from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"NAME: {self.name}; "
            f"CHAT ID: {self.id}; "
        )


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"CHAT {self.chat}; "
            f"DATE: ({self.created_at:%Y-%m-%d %H:%M}): "
            f"USER: {self.user}; "
            f"MESSAGE: {self.text}"
        )
