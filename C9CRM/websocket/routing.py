# -*- coding: utf-8 -*-  
from django.conf.urls import url

from . import consumer

websocket_urlpatterns = [
    url(r'^ws/chat/xupan/$', consumer.ChatConsumer),
]