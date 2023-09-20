from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.TextField()
    message_date = models.TextField()
