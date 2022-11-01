from pythonosc.dispatcher import Dispatcher

import pyautogui as p 
from time import sleep
import string

alphabet = list(string.ascii_lowercase)
for i, letter in enumerate(alphabet):
    alphabet[i] = (str(i),letter)

alphabet = dict(alphabet)
# alphabet_dict = dict(zip(enumerate(alphabet))


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

    


def playSound(key, wait=0.05, use_alphabet=False):
    global alphabet
    global opened
    

    if opened == False:
        opened = openAbleton()

    if use_alphabet == True:

        print(f"{alphabet.get(key)} pressed")
        p.keyDown(str(alphabet.get(key)))
        

    else:

        p.keyDown(str(key))
        print(f"{key} pressed")

    sleep(wait)
    
# playSound(alphabet['2'], use_alphabet= True)

def mapSoundNumber(address: str, *args):
    
    msg_index = address[-1] 
    msg_value = args[0]
    if msg_value > 0:
        playSound(msg_index)

def mapSoundAlphabet(address: str, *args):
    
    msg_index = address[-1]
    msg_value = args[0]

    if msg_value > 0:
        playSound(msg_index,use_alphabet = True)
    

def print_handler(address, *args):
    print(f"{address}: {args}")

# def default_handler(address, *args):
#     print(f"DEFAULT {address}: {args}")

dispatcher = Dispatcher()

#play sound 1 for 1 second
dispatcher.map("/sound/*", mapSoundNumber)
dispatcher.map("/AIVOICE/*", mapSoundAlphabet)

# dispatcher.set_default_handler(default_handler)