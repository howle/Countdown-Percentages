import time
import datetime
from termcolor import colored

countdown = 30
while countdown > 0:
    percentage = countdown / 30
    color = None
    if percentage <= 0.2:
        color = 'red'
    elif percentage <= 0.5:
        color = 'yellow'
    else:
        color = 'green'
    print('\r' + ' '*10 + colored(str(countdown).zfill(2), color), end='')
    time.sleep(1)
    countdown -= 1

print('\r' + ' '*10 + colored('LETS GO', 'green'), datetime.datetime.now().strftime(' %Y-%m-%d %H:%M:%S'))
