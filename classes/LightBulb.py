import socket


class LightBulb:

    def __init__(self):
        self.socket_conn = socket.socket()

        self.light_name = ''
        self.name = ''  # how this gets populated from lamp?
        self.model = ''
        self.address = tuple()
        self.properties = list()
        self.power = ''
        self.bright = ''
        self.color_mode = ''
        self.ct = ''  # TODO what is this?
        self.rgb = ''
        self.hue = ''
        self.sat = ''

    def fill_data_from_discover(self, info_in_bytes):
        light_properties = info_in_bytes[0].decode('utf-8').split('\r\n')

        current_lamp_properties = dict()
        for lamp_properties_item in light_properties:
            properties = lamp_properties_item.split(':', 1)
            if len(properties) == 2:
                if properties[0] == 'support':
                    current_lamp_properties[properties[0]] = list(filter(None, properties[1].split(' ')))
                    continue
                current_lamp_properties[properties[0]] = properties[1].strip()
            else:
                # If key has no value, continue
                continue

        print(self.name)
        # print(self.__dict__)

        self.name = 'test'
        a = 'name'
        self.__dict__[a] = 'test2'

        print(self.name)
        print(current_lamp_properties)


