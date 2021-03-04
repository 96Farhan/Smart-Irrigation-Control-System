"""
Module Name: routing
Descriptipn: Path for Websocket URL Router.
"""


from channels.routing import ProtocolTypeRouter, ChannelNameRouter
from iot.consumers import MqttConsumer

application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "mqtt": MqttConsumer
    }),
})