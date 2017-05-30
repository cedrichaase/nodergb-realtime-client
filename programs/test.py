from colour import Color
from rgbc_rt import RGBCRt
from time import sleep

client = RGBCRt('127.0.0.1', 1337)


def set_color(color):
    client.set_color(Color(color))


def transition(color1, color2, time):
    color1, color2 = Color(color1), Color(color2)

    for color in color1.range_to(color2, time * 50):
        set_color(color)
        sleep(0.02)


def cycle(colors, cycle_time=10, wait=0.1):
    """
    Cycles through a list of colors
    
    :param colors:      The list of colors to cycle through
    :param cycle_time:  Time the entire cycle should take
    :param wait:        Time to wait after each part of the cycle
    :return: 
    """
    transition_time = max(int(cycle_time / len(colors)), 1)

    for i, color in enumerate(colors):
        next = (i + 1) % len(colors)
        transition(color, colors[next], transition_time)
        sleep(wait)


def pulse(color, cycle_time=1, pulse_distance=1.2):
    set_color('black')
    cycle([Color(color, luminance=0.001), color], cycle_time=cycle_time, wait=0)
    set_color('black')
    sleep(pulse_distance)


while True:
    pulse('purple', 3)

