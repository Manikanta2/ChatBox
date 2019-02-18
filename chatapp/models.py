from django.utils import timezone
from django.db import models
import uuid
from django.contrib.auth.models import User


class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class ChatBox(models.Model):
    group_name = models.CharField(max_length=200)
    group_description = models.TextField(max_length=420, editable=True, default='Required')
    group_ID = models.CharField(unique=True, default=uuid.uuid4, editable=False, max_length=50, primary_key=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


class Message(models.Model):
    message_ID = models.CharField(unique=True, default=uuid.uuid4, editable=False, max_length=50, primary_key=True)
    message_tag = models.CharField(max_length=100)
    message_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    to_group = models.ForeignKey(
        ChatBox, on_delete=models.CASCADE)

    def __str__(self):
        return self.message_text


class Connected(models.Model):
    group_ID = models.ForeignKey(ChatBox, on_delete=models.CASCADE)
    message_ID = models.ForeignKey(Message, on_delete=models.CASCADE)

