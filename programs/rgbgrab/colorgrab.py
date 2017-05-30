import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk


class ColorGrabber:

    # process every nth pixel from the buffer
    process_each = 192

    def __init__(self):
        self. win = Gdk.get_default_root_window()
        self.h = self.win.get_height()
        self.w = self.win.get_width()
        self.num_colors = (self.w * self.h) / self.process_each

    def grab(self):
        pixelbuffer = Gdk.pixbuf_get_from_window(self.win, 0, 0, self.w, self.h)

        pixel_bytes = pixelbuffer.read_pixel_bytes()

        pixels = pixel_bytes.get_data()

        r_avg, b_avg, g_avg = 0, 0, 0

        for i in range(0, len(pixels), 3 * self.process_each):
            r_avg += pixels[i]
            g_avg += pixels[i+1]
            b_avg += pixels[i+2]

        r_avg = int(r_avg / self.num_colors)
        g_avg = int(g_avg / self.num_colors)
        b_avg = int(b_avg / self.num_colors)

        return r_avg, g_avg, b_avg
        #return "#{:02x}{:02x}{:02x}".format(r_avg, g_avg, b_avg)
