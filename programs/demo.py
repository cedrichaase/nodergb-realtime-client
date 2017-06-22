from rgb import *
from multiprocessing import Process
from time import sleep


def strobe_1(host):
    while True:
        set_color('blue', host=host)
        sleep(0.5)
        set_color('black', host=host)
        sleep(0.5)
        set_color('red', host=host)
        sleep(0.5)


def strobe_2(host):
    while True:
        set_color('red', host=host)
        sleep(0.2)
        set_color('white', host=host)
        sleep(0.1)


def stuff(host):
    while True:
        pulse('purple', 3, host=host)
        transition('green', 'red', 3, host=host)
        pulse('white', 0.5, host=host)
        cycle(['orange', 'white', 'purple', 'red', 'green'], 60, host=host)
        set_color('red', host=host)
        sleep(60)


p1 = Process(target=strobe_1, args=('eingang.0',))
p2 = Process(target=strobe_2, args=('eingang.1',))

p3 = Process(target=stuff, args=('buehne.0',))
p4 = Process(target=strobe_2, args=('buehne.1',))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

    # set_color('black', host='bett')
    # sleep(0.1)
    # set_color('white', host='sofa')
    # sleep(0.1)
    #
    # set_color('red', host='bett')
    # sleep(0.1)
    # set_color('blue', host='sofa')
    # sleep(0.1)
    #
    # set_color('black', host='bett')
    # sleep(0.1)
    # set_color('white', host='sofa')
    # sleep(0.1)
    #
    # set_color('red', host='sofa')
    # sleep(0.1)
    # set_color('blue', host='bett')
    # # sleep(0.1)
    #
    # p1 = Process(target=cycle, args=(['#f0c', '#0fc', '#fc0'], 10, 1, 'sofa'))
    # p2 = Process(target=cycle, args=(['#0fc', '#fc0', '#f0c'], 10, 1, 'bett'))
    #
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    #
    # set_color('red')
    # sleep(10)
