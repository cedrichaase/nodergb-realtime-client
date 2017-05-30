import struct
import Quartz.CoreGraphics as CG


class ColorGrabber:

    # process every nth pixel from the buffer
    process_each = 200

    # dpi
    dpi = 227

    def __init__(self):
        entire_screen = CG.CGRectInfinite
        image = CG.CGWindowListCreateImage(
            entire_screen,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault)

        width = CG.CGImageGetWidth(image)
        height = CG.CGImageGetHeight(image)
        self.region = CG.CGRectMake(250, 250, 800, 600)
        pass

    def grab(self):
        # Create screenshot as CGImage
        image = CG.CGWindowListCreateImage(
            self.region,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault)

        # Intermediate step, get pixel data as CGDataProvider
        prov = CG.CGImageGetDataProvider(image)

        # Copy data out of CGDataProvider, becomes string of bytes
        self._data = CG.CGDataProviderCopyData(prov)

        num_colors = len(self._data) / 4 / self.process_each

        # Pixel data is unsigned char (8bit unsigned integer),
        # and there are for (blue,green,red,alpha)
        data_format = "BBBB"

        r_avg, b_avg, g_avg = 0, 0, 0

        for i in range(0, len(self._data), 4 * self.process_each):
            b, g, r, a = struct.unpack_from(data_format, self._data, offset=i)
            r_avg += r
            g_avg += g
            b_avg += b

        r_avg = int(r_avg / num_colors / 2)
        g_avg = int(g_avg / num_colors / 2)
        b_avg = int(b_avg / num_colors / 2)

        #return "#{:02x}{:02x}{:02x}".format(r_avg, g_avg, b_avg)
        return r_avg, g_avg, b_avg