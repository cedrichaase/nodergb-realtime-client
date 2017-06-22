from rgb import *
from time import time

while True:
    set_color('white')
    set_color('black')
    wait = (time() - int(time()))
    print(wait)
    sleep(wait)
