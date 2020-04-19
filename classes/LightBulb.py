import socket


class LightBulb:

    def __init__(self):
        self.socket_conn = socket.socket()

        self.light_name = ''
        self.model = ''
        self.address = tuple()
        self.properties = list()
        self.power = ''
        self.bright = 0
        self.color_mode = ''
        self.ct = ''  # TODO what is this?
        self.rgb = ''
        self.hue
        self.sat
        self.name
