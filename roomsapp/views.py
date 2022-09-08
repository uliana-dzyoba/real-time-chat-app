from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Room, Message


@login_required
def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'roomsapp/rooms.html', {'rooms': rooms})


@login_required
def get_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'roomsapp/room.html', {'room': room, 'messages': messages})