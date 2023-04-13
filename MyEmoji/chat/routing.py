from django.urls import path
from chat import consumers
# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
# ]

websocket_urlpatterns = [
    path("ws/chat/<str:room_pk>/chat/", consumers.ChatConsumer.as_asgi()),
]
