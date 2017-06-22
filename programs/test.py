from rgb import *

while True:
    pulse('purple', 3)
    transition('green', 'red', 3)
    pulse('white', 0.5)
    cycle(['orange', 'white', 'purple', 'red', 'green'], 60)
    set_color('red')
    sleep(60)
