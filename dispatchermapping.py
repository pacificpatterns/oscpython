from pythonosc.dispatcher import Dispatcher

import pyautogui as p 
from time import sleep

# class Ableton(object):
#     def __init__(self,self.open):
#         self.open = False

#     def opened(self):
#         self.open = True
# ableton = Ableton()
opened = False
def openAbleton():
    p.keyDown("command")
    p.press('space')
    p.keyUp("command")
    p.write('ableton')
    p.press('enter')
    global opened
    opened = True
    return opened

    


def playSound(key, wait):
    global opened
    if opened == False:
        opened = openAbleton()

    key = str(key)
    p.keyDown(key)
    print(f"{key} pressed")
    sleep(wait)
    

def mapSound(address: str, *args):
    
    index = address[-1]

    value = args[0]
    if value > 0:
        playSound(index,0.005)
    

def print_handler(address, *args):
    print(f"{address}: {args}")

# def default_handler(address, *args):
#     print(f"DEFAULT {address}: {args}")

dispatcher = Dispatcher()

#play sound 1 for 1 second
dispatcher.map("/sound/*", mapSound)

# dispatcher.set_default_handler(default_handler)