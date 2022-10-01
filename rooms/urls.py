from django.urls import path

from . import views

app_name = "chats"

urlpatterns = [
    path('private/', views.list_private_chats, name='private_chats'),
    path('private/<str:username>/', views.get_private_chat, name='private_chat'),
    path('', views.list_rooms, name='rooms'),
    path('<slug:slug>/', views.get_room, name='room'),
]
