from django.contrib.auth.models import User, Group
from django.http import Http404
from django.shortcuts import render
from .models import ChatBox, Userinfo, Connected


def home(request):
    all_groups = ChatBox.objects.all()
    return render(request, 'home.html', {'groups': all_groups})


def profile(request, username):
    if User.objects.get(username=username):
        profile = Userinfo.objects.get(user=User.objects.get(username=username))
    return render(request, 'user.html', {'users': profile})


def group_details(request, group_id):
    group = ChatBox.objects.get(pk=group_id)
    my_msg = Connected.objects.get(pk=group_id)
    return render(request, 'group.html', {'group': group, 'my_msg': my_msg})


def register_group(request, my_group_name):
    my_group = Group.objects.get(name=my_group_name)
    my_group.user_set.add(User)
    return render(request, 'group.html', {'my_group': my_group})








