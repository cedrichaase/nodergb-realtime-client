from colour import Color
import socket


class RGBCRt:
    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.connect((address, port))
        self.socket.settimeout(0.0333)

    @staticmethod
    def __format_color(color):
        hex_color = bytes(color.get_hex_l()[1:] + "\n", "utf8")
        return hex_color

    @staticmethod
    def __format_packet(color, host=''):
        content = "{0}{1}{2}\n".format(host, ':' if host else '', color)
        return bytes(content, "utf8")

    def set_color(self, color, host=''):
        self.socket.sendall(self.__format_packet(color, host))

    def set_timeout(self, timeout):
        self.socket.settimeout(timeout)
