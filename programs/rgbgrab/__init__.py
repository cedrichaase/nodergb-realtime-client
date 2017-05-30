import sys
from time import sleep

if sys.platform.startswith('linux'):
    from rgbgrab.colorgrab import ColorGrabber
elif sys.platform == 'win32':
    from rgbgrab.colorgrab_win import ColorGrabber
elif sys.platform == 'darwin':
    from rgbgrab.colorgrab_osx import ColorGrabber
else:
    raise ImportError('Unsupported platform ' + sys.platform)


class Grabber:

    # previously grabbed color
    # prev_color = '#000000'
    rgb_prev = (0, 0, 0)

    # current frequency
    freq = 120

    # minimum frequency
    freq_min = 0.5

    # max frequency
    freq_max = 60

    # period
    period = 1 / freq

    def __init__(self, client):
        self.grabber = ColorGrabber()
        self.client = client

    def colors_differ(self, a, b):
        for i in range(0, 3):
            if a[i] > b[i] + 1 or a[i] < b[i] - 1:
                return True

    def grab_color(self):
        rgb = self.grabber.grab()

        if self.colors_differ(rgb, self.rgb_prev):
            self.rgb_prev = rgb
            hex_color = "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
            self.client.set_rgb(hex_color)
            self.set_freq(self.freq_max)
        else:
            self.set_freq(max(self.freq * 0.99, self.freq_min))

    def run(self):
        while True:
            sleep(self.period)
            self.grab_color()

    def set_freq(self, freq):
        self.freq = freq
        self.period = 1/freq
