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

print(lamp)