"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""


import os
import django
from channels.routing import get_default_application
from channels.layers import get_channel_layer
# import channels.layers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iot_platform.settings")
django.setup()

# Application
application = get_default_application()

# Layers
channel_layer = get_channel_layer()

