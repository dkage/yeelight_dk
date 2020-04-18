import socket
import sys


def discover_lights(timeout=2):
    """
    This function multicast a package, looking for Yeelight devices in the local network.

    :param timeout: time for package timeout
    :return: yeelight devices
    """
    message = "\r\n".join(['M-SEARCH * HTTP/1.1',
                           'HOST: 239.255.255.250:1982',
                           'MAN: "ssdp:discover"',  # the internal MAN value needs to be using double quotes
                           'ST: wifi_bulb'])

    # CREATING SOCKET:
    # AF_INET -> Sets socket for IPv4 protocol
    # SOCK_DGRAM -> Sets socket for UDP communication, one way, datagram-based protocol. Ie.: 1 packet, 1 response.
    # IPPROTO_UDP -> Improve checksum failure for UDP packet
    discover_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # SETTING OPTIONS FOR SOCKET:
    # IPPROTO_IP -> #TODO needs research, need better understanding
    # IP_MULTICAST_TTL -> Sets socket for multicast communication type
    discover_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    discover_socket.settimeout(timeout)

    yeelight_multicast_address = "239.255.255.250"
    yeelight_port = 1982

    # Message needs encoding to bytes, UTF-8 is not valid
    discover_socket.sendto(message.encode(), (yeelight_multicast_address, yeelight_port))

    try:
        # Value 65535 = 65,535 bytes (8 byte header + 65,527 bytes of data) for a UDP datagram
        lamps_discovered = discover_socket.recvfrom(65507)
    except socket.timeout:
        # TODO make better error handling here. Needs retrying.
        print('error')
        sys.exit('error, no lamp found')

    return lamps_discovered


print(discover_lights())



