import socket


class LightBulb:

    def __init__(self):
        self.socket_conn = socket.socket()

        self.light_name = ''
        self.name = ''  # how this gets populated from lamp?
        self.model = ''
        self.address = tuple()
        self.supported_functions = list()
        self.power = ''
        self.bright = ''
        self.color_mode = ''
        self.ct = ''  # TODO what is this?
        self.rgb = ''
        self.hue = ''
        self.sat = ''
        self.id = ''

    def fill_data_from_discover(self, info_in_bytes):
        light_properties = info_in_bytes[0].decode('utf-8').split('\r\n')

        current_lamp_properties = dict()
        for lamp_properties_item in light_properties:
            properties = lamp_properties_item.split(':', 1)
            if len(properties) == 2:
                if properties[0] == 'support':
                    current_lamp_properties['supported_functions'] = list(filter(None, properties[1].split(' ')))
                    continue
                current_lamp_properties[properties[0]] = properties[1].strip()
            else:
                # If key has no value, continue
                continue

        # Grab value "yeelight://<ip>:<port>", grabs only <ip>:<port> section, then splits by :
        address_info = current_lamp_properties['Location'].split('/', -1)[2].split(':')
        self.address = address_info[0], int(address_info[1])

        # If there is a self.variable_name with same key name in dict, class instance receives that value
        for key, value in current_lamp_properties.items():
            if key in self.__dict__:
                self.__dict__[key] = value