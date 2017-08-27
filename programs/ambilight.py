from colour import Color
from rgbc_rt import RGBCRt
from rgbgrab import Grabber

client = RGBCRt('192.168.178.2', 1337)
grabber = Grabber(client)
grabber.run()
