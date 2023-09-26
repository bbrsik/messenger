from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.name} "
            f"{self.id} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
        )


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.chat} "
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.text[:30]}..."
        )
