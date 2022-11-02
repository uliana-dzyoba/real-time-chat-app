from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Room, Message

default_pfp = 'rooms/images/default-avatar.jpg'


@login_required
def list_rooms(request):
    qs = Room.objects.filter(private_chat=False)
    rooms = []
    for room in qs:
        message = Message.objects.filter(room=room).first()
        rooms += [{'room': room, 'message': message}]
    return render(request, 'rooms/rooms.html', {'chats': rooms, "dpfp": default_pfp})


@login_required
def get_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)[0:25:-1]
    return render(request, 'rooms/room.html', {'room': room, 'messages': messages, "dpfp": default_pfp})


@login_required
def list_private_chats(request):
    qs = Room.objects.filter(private_chat=True, slug__contains=request.user.username)
    chats = []
    for room in qs:
        username = room.slug.replace(request.user.username, '')
        receiver = User.objects.get(username=username)
        message = Message.objects.filter(room=room).first()
        chats += [{'receiver': receiver, 'message': message}]
    return render(request, 'rooms/private_chats.html', {'chats': chats, "dpfp": default_pfp})


@login_required
def get_private_chat(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)
    first, second = sorted([sender.username, receiver.username])
    slug = first + second
    room_qs = Room.objects.filter(slug=slug)
    if room_qs.exists():
        room = room_qs[0]
    else:
        name = first.capitalize() + second.capitalize()
        room = Room.objects.create(name=name, slug=slug, private_chat=True)
    messages = Message.objects.filter(room=room)[0:25:-1]
    return render(request, 'rooms/room.html', {'room': room, 'username': username, 'messages': messages, "dpfp": default_pfp})
