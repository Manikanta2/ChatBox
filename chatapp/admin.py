from django.contrib import admin
from .models import ChatBox, Userinfo, Connected, Message

admin.site.register(ChatBox)
admin.site.register(Connected)
admin.site.register(Message)
admin.site.register(Userinfo)
