import json
from channels.generic.websocket import AsyncWebsocketConsumer




class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connect....')
        self.room_group_name = 'sensor_temperature'
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self,mqtt_message):
        print(mqtt_message["payload"])
        await self.send(text_data=json.dumps({"message": mqtt_message}))
        pass

    # Receive message from group
    async def sensor_temperature(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message['payload']}))



    async def disconnect(self, close_code):
        pass

