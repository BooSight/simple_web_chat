"""
ASGI config for first_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

from email.mime import application
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_chat.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application()
})