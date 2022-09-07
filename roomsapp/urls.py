from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_rooms, name='rooms'),
    path('<slug:slug>/', views.get_room, name='room'),
]
