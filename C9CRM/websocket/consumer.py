# -*- coding: utf-8 -*-  
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print(self)
        self.room_name = 'xupan'
        self.room_group_name = 'chat_%s' % self.room_name

        # 加入组
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.scope.get('user_info'))
        if self.scope.get('user_info'):
            self.accept()
        else:
            self.send(text_data=json.dumps({
                'message': 'wrong connect'
            }))
    def disconnect(self, close_code):
        # 离开组
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 将一个事件发送给一个组
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))