# from ctypes import windll
# dc = windll.user32.GetDC(0)

import pyscreenshot as ImageGrab

class ColorGrabber:
    process_each = 256

    def __init__(self):
        self.width = 1920
        self.height = 1080

        self.num_colors = (self.width / self.process_each) * (self.height / self.process_each)
        pass

    def grab(self):
        pixels = ImageGrab.grab().load()

        r_avg, g_avg, b_avg = 0, 0, 0

        for x in range(0, self.width, self.process_each):
            for y in range(0, self.height, self.process_each):
                pixel = pixels[x, y]
                r_avg += pixel[0]
                g_avg += pixel[1]
                b_avg += pixel[2]

        r_avg = int(r_avg / self.num_colors)
        g_avg = int(g_avg / self.num_colors)
        b_avg = int(b_avg / self.num_colors)

        hex_color = "#{:02x}{:02x}{:02x}".format(r_avg, g_avg, b_avg)
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        return r, g, b

