import socket
import sys
import json
from urllib.parse import urlparse


timeout = 2

msg = "\r\n".join(["M-SEARCH * HTTP/1.1", "HOST: 239.255.255.250:1982", 'MAN: "ssdp:discover"', "ST: wifi_bulb"])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

s.settimeout(timeout)
s.sendto(msg.encode(), ("239.255.255.250", 1982))

try:
    lamp = s.recvfrom(65507)
except socket.timeout:
    print('error')
    sys.exit('error, no lamp found')

# BULB dict creation after discover
bulb = dict()

# not assigning lamp values direct to bulb to later make changes for when more than 1 bulb in lan (currently only 1)
bulb['ip'] = "0.0.0.0"
bulb['port'] = "0000"
bulb['properties'] = list()

bulb['address'] = lamp[1][0], 55443
bulb['port'] = lamp[1][1]

lamp_properties_list = lamp[0].decode('utf-8').split('\r\n')


current_lamp_properties = dict()
for lamp_properties_item in lamp_properties_list:
    properties = lamp_properties_item.split(':', 1)
    if len(properties) == 2:
        if properties[0] == 'support':
            current_lamp_properties[properties[0]] = list(filter(None, properties[1].split(' ')))
            continue
        current_lamp_properties[properties[0]] = properties[1]
    else:
        # If key has no corresponding value, continue
        continue

bulb['properties'] = current_lamp_properties

socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_conn.connect(bulb['address'])

# Yeelight documentation states that commands should be passed as JSON, following this structure
# { "id": 1, "method": "set_power", "params":["on", "smooth", 500]}
command = {"id": 1, "method": "set_power", "params": ["on", "smooth", 500]}
command_json = (json.dumps(command) + '\r\n').encode('utf-8')

socket_conn.send(command_json)

