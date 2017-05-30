from colour import Color
from rgbc_rt import RGBCRt
from time import sleep

client = RGBCRt('127.0.0.1', 1337)


def transition(color1, color2, time):
    color1 = Color(color1)
    color2 = Color(color2)

    for color in color1.range_to(color2, time * 50):
        client.set_color(color)
        sleep(0.02)


def cycle(colors, cycle_time=10, wait=0.1):
    transition_time = min(int(cycle_time / len(colors)), 1)

    for i, color in enumerate(colors):
        next = (i + 1) % len(colors)
        print(color, colors[next], i, next)
        transition(color, colors[next], transition_time)
        sleep(wait)


while True:
    cycle(['blue', 'red', 'green'], 10)

