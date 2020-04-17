import socket


class LightBulb:

    def __init__(self):
        self.light_location = ''
        self.socket_conn = socket.socket()
        self.address = tuple()
        self.properties = list()
