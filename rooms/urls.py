from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_rooms, name='rooms'),
    path('<slug:slug>/', views.get_room, name='room'),
    path('private/', views.list_private_chats, name='private_chats'),
    path('private/<str:username>/', views.get_private_chat, name='private_chat')
]
