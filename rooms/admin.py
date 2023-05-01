from django.contrib import admin

from .models import Room, Message


class MessageInline(admin.TabularInline):
    extra = 1
    model = Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [
        MessageInline,
    ]

admin.site.register(Message)
