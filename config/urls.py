from django.contrib import admin
from django.urls import path,include
from notification.consumers import NotificationConsumer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("notification.urls")),
]


websocket_urlpatterns = [
    path("ws/notifications/",NotificationConsumer.as_asgi()),
]