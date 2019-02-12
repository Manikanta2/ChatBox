from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from .models import ChatBox, Userinfo


def home(request):
    all_groups = ChatBox.objects.all()
    return render(request, 'home.html', {'groups': all_groups})

def profile(request, username):
    if User.objects.get(username=username):
        profile = Userinfo.objects.get(user=User.objects.get(username=username))
    return render(request, 'user.html', {'users': profile})

def group_details(request, group_id):
    try:
        group = ChatBox.objects.get(pk=group_id)
    except group.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'group.html', {'group': group})





