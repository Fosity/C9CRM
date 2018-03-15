# -*- coding: utf-8 -*-  
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import websocket.routing
from carry import models

class QueryAuthMiddleware:
    """
    Custom middleware (insecure) that takes user IDs from the query string.
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):
        try:
            session_values = scope.get('session').values()[0]
        except:
            session_values='False'
        scope['user_info']=session_values
        return self.inner(scope)


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': QueryAuthMiddleware(
        URLRouter(
            websocket.routing.websocket_urlpatterns
        )
    ),
})