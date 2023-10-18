from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"NAME: {self.name}; "
            f"ID: {self.id}; "
        )


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply_on = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def get_replies_chain(self):
        # todo получить массив объектов Message() для всей цепочки ответов
        class Node:
            def __init__(self, data, prev=None):
                self.data = data
                self.prev = prev

        head = Node(Message(self))
        current = head
        while current is not None:
            current.prev = Message.objects.get(reply_on=current.prev)
            current = current.prev

        current = head
        reply_array = []
        while current is not(None):
            reply_array.append(current.data)
            current = current.prev
        return reply_array

    def __str__(self):
        return (
            f"CHAT: {self.chat}; "
            f"USER: {self.user}; "
            f"DATE: ({self.created_at:%Y-%m-%d %H:%M}): "
            f"MESSAGE: {self.text[:30]}..."
        )


