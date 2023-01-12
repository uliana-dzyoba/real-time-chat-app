from django.shortcuts import render
from django.contrib.auth.models import User

from rooms.models import Room, Message

default_pfp = 'rooms/images/default-avatar.jpg'


# Create your views here.
def get_frontpage(request):
    if request.user.is_authenticated:
        messages = Message.objects.filter(user=request.user)[0:5:-1]
        room_list = [message.room for message in messages]
        rooms = set(room_list)
        chats = []
        for room in rooms:
            message = Message.objects.filter(room=room).first()
            if room.private_chat:
                username = room.slug.replace(request.user.username, '')
                receiver = User.objects.get(username=username)
                chats += [{'private': True, 'receiver': receiver, 'message': message}]
            else:
                chats += [{'private': False, 'room': room, 'message': message}]
        return render(request, 'main/frontpage.html', {'chats': chats, "dpfp": default_pfp})
    else:
        return render(request, 'main/frontpage.html')
