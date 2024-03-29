from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=25, unique=True)
    private_chat = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', null=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=100000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
