import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass  # Handle disconnection if needed

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        # Extract sensor readings
        flow_value = data.get('flow')
        temperature_value = data.get('temperature')
        pressure_value = data.get('pressure')

        # Broadcast the data to all connected clients
        await self.send(text_data=json.dumps({
            'flow': flow_value,
            'temperature': temperature_value,
            'pressure': pressure_value
        }))
