from channels.generic.websocket import AsyncWebsocketConsumer
from django.template import Context, Template
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    # accept connection

    async def connect(self):
        await self.accept()

        # add user to group
        await self.channel_layer.group_add(
            "notification",self.channel_name
        )

    # define wat happens when user disconnects
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            "notification",self.channel_name
        )

    # define method to send notification
    async def send_notification(self,event):
        message = event["message"]

        template = Template(
            "<div class='notification'><p>{{message}}</p></div>"
        )

        context = Context({"message":message})
        render_notification = template.render(context)

        await self.send(
            text_data=json.dumps(
                {
                    "type":"notification",
                    "message":message
                }
            )
        )

