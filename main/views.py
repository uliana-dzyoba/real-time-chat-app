from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse

from rooms.models import Message

default_pfp = 'images/default_avatar.jpg'

NUMBER_OF_MESSAGES = 5


# Create your views here.
def get_frontpage(request):
    if request.user.is_authenticated:
        messages = Message.objects.filter(user=request.user)[0:NUMBER_OF_MESSAGES:-1]
        rooms = set([message.room for message in messages])
        if not rooms:
            return redirect(reverse('chats:rooms'))
        chats = []
        for room in rooms:
            message = room.messages.all().first()
            if room.private_chat:
                username = room.slug.replace(request.user.username, '')
                receiver = User.objects.get(username=username)
                chats += [{'private': True, 'receiver': receiver, 'message': message}]
            else:
                chats += [{'private': False, 'room': room, 'message': message}]
        return render(request, 'main/frontpage.html', {'chats': chats, "dpfp": default_pfp})
    else:
        return render(request, 'main/frontpage.html')
