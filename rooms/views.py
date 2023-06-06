from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from chatproject.settings import DEBUG
from .models import Room, Message
from .utils import split_dates

default_pfp = 'images/default_avatar.jpg'

NUMBER_OF_MESSAGES = 25

PROTOCOL = 'ws' if DEBUG else 'wss'

@login_required
def list_rooms(request):
    qs = Room.objects.filter(private_chat=False)
    rooms = []
    for room in qs:
        message = Message.objects.filter(room=room).first()
        rooms += [{'room': room, 'message': message}]
    return render(request, 'rooms/rooms.html', {'chats': rooms, 'dpfp': default_pfp})


@login_required
def get_room(request, slug):
    room = get_object_or_404(Room, slug=slug, private_chat=False)
    messages = room.messages.all()[0:NUMBER_OF_MESSAGES:-1]
    split_dates(messages)
    return render(request, 'rooms/room.html', {'room': room, 'messages': messages, 'dpfp': default_pfp, 'protocol': PROTOCOL})


@login_required
def list_private_chats(request):
    qs = Room.objects.filter(private_chat=True, slug__contains=request.user.username)
    chats = []
    for room in qs:
        username = room.slug.replace(request.user.username, '')
        receiver = User.objects.get(username=username)
        message = room.messages.all().first()
        chats += [{'receiver': receiver, 'message': message}]
    return render(request, 'rooms/private_chats.html', {'chats': chats, 'dpfp': default_pfp})


@login_required
def get_private_chat(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)
    first, second = sorted([sender.username, receiver.username])
    slug = first + second
    room = Room.objects.filter(slug=slug).first()
    if not room:
        name = first.capitalize() + second.capitalize()
        room = Room.objects.create(name=name, slug=slug, private_chat=True)
    messages = room.messages.all()[0:NUMBER_OF_MESSAGES:-1]
    split_dates(messages)
    return render(request, 'rooms/room.html', {'room': room, 'username': username, 'messages': messages, 'dpfp': default_pfp, 'protocol': PROTOCOL})
