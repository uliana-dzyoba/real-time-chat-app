from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Room, Message


@login_required
def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms.html', {'rooms': rooms})


@login_required
def get_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    default_pfp = settings.MEDIA_URL + 'images/default-avatar.jpg'
    return render(request, 'rooms/room.html', {'room': room, 'messages': messages, "dpfp": default_pfp})