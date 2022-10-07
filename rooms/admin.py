from django.contrib import admin

from .models import Room, Message


class MessageInline(admin.TabularInline):
    model = Message


class RoomAdmin(admin.ModelAdmin):
    inlines = [
        MessageInline,
    ]


admin.site.register(Message)
admin.site.register(Room, RoomAdmin)
