from PIL import Image

class ImageColorGrabber:

    def __init__(self):
        pass

    def grab(self, image_file):
        image = Image.open(image_file, 'r')
        pixels = list(image.getdata())

        r_avg, b_avg, g_avg = 0, 0, 0

        num_colors = len(pixels) / 256

        for i in range(0, len(pixels), 256):
            r_avg += pixels[i][0]
            g_avg += pixels[i][1]
            b_avg += pixels[i][2]

        r_avg = int(r_avg / num_colors)
        g_avg = int(g_avg / num_colors)
        b_avg = int(b_avg / num_colors)

        return "#{:02x}{:02x}{:02x}".format(r_avg, g_avg, b_avg)
