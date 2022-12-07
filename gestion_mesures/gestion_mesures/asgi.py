"""
ASGI config for mqtt_tuto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from django.core.asgi import get_asgi_application


from mqtt_topics.consumers import MyMqttConsumer

from dashboardapp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_mesures.settings')

django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter({
        'http': django_asgi_app,
        'mqtt': MyMqttConsumer.as_asgi(),
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
})
