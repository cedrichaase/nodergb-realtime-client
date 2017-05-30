from colour import Color
from rgbc_rt import RGBCRt
from rgbgrab import Grabber

client = RGBCRt('127.0.0.1', 1337)
grabber = Grabber(client)
grabber.run()
