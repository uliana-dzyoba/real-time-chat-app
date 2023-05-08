import json
import asyncio
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from django.utils import timezone

from .models import Room, Message


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        if close_code is not None and close_code != 1000:
            await asyncio.sleep(5)
            await self.connect()

    # Receive message from WebSocket
    async def receive_json(self, content):
        message = content['message']
        username = content['username']
        pfp = content['pfp']

        await self.save_message(username, self.room_name, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
                'username': username,
                'pfp': pfp,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        timestamp = timezone.localtime(timezone.now())
        time = timestamp.strftime("%H:%M")
        content = {**event, 'time': time}

        # Send message to WebSocket
        await self.send_json(content=content)

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        Message.objects.create(user=user, room=room, content=message)
