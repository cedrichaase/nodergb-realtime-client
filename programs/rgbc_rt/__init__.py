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

    def set_color(self, color):
        self.socket.sendall(self.__format_color(color))

    def set_timeout(self, timeout):
        self.socket.settimeout(timeout)

    def set_rgb(self, hex_color):
        self.socket.sendall(bytes(hex_color + "\n", "utf8"))