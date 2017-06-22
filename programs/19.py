from rgb import *
from time import sleep

for x in range(369):
    divide = x/19
    if divide == 11:
        set_color("#FF1493")
    elif divide == 12:
        set_color("#C71585")
    elif divide == 13:
        set_color("#BF3BFF")
    elif divide == 14:
        set_color("#FFDEAD")
    elif divide == 15:
        set_color("#FFB90F")
    elif divide == 16:
        set_color("#FFD700")
    elif divide == 17:
        set_color("#7FFF00")
    elif divide == 18:
        set_color("#F0E68C")
    elif divide == 19:
        set_color("#FFC1C1")
    else:
        set_color("#00CED1")
    sleep(1)
    
set_color("#000")

"""
alle Zahlen von 1 bis 369 durch 19
wenn das Ergebnis eine Zahl zwischen 11 und 19 ist werden jeweils die den Zahlen
zugewiesenen Farben gezeigt
wenn das Ergebnis nicht eine Zahl zwischen 11 und 19 ist wird eisblau angezeigt
solange 1 bis 369 ist true dann ab 370 false und das Dings ist fertig (LEDs aus)
Pause zwischen den Zahlen jeweils 1 Sekunde
"""