from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.text[:30]}..."
        )
