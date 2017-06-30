from channels.routing import route
from .consumers import incoming, online, offline

channel_routing = [
    route("websocket.connect", incoming, path=r"^/incoming/$"),
    route("websocket.connect", online, path=r"^/online/$"),
    route("websocket.disconnect", offline, path=r"^/online/$"),

        ]
