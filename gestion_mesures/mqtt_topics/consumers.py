from mqttasgi.consumers import MqttConsumer
from persistanceapp.persistance_engine import persistData

class MyMqttConsumer(MqttConsumer):
    async def connect(self):
        await self.subscribe('sensor/temperature', 2)
        self.room_group_name = 'sensor_temperature'
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    async def receive(self, mqtt_message):
        print('Received a message at topic:', mqtt_message['topic'])
        print('With payload', mqtt_message['payload'])
        print('And QOS:', mqtt_message['qos'])
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "sensor.temperature",
                "message": {"payload": mqtt_message['payload'].decode("utf-8")}
            }
        )
        pass
    #Receive message from group
    async def sensor_temperature(self, event):
        message = event["message"]
        # push message to database
        persistData(message['payload'])
        pass

    async def disconnect(self):
        await self.unsubscribe('sensor/temperature')