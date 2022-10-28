from pythonosc.dispatcher import Dispatcher

import pyautogui as p 
from time import sleep
from typing import List, Any

open = False

def openAbleton():
    p.keyDown("command")
    p.press('space')
    p.keyUp("command")
    p.write('ableton')
    p.press('enter')
    return True

def playSound(key, wait):
    if not open:
        open = openAbleton()

def mapSound(address: str, *args):
    
    # key = str(args[0])
    # wait = args[1]
    # p.keyDown(key)
    # print(f"{key} pressed")
    # sleep(wait)
    # message_value
    index = address[-1]
    print(f"{index} is the index")
    value = args
    # if value > 0:
    #     playSound
    print(args)
    print(address)

def print_handler(address, *args):
    print(f"{address}: {args}")

# def default_handler(address, *args):
#     print(f"DEFAULT {address}: {args}")

dispatcher = Dispatcher()

#play sound 1 for 1 second
dispatcher.map("/sound/2", mapSound,1)

# dispatcher.set_default_handler(default_handler)