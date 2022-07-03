from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/socket-server/posts/<int:id>', consumers.PostConsumer.as_asgi()),
    path('ws/socket-server/admin/users', consumers.UserConsumer.as_asgi())
]