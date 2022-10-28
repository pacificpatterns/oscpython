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
    open = True

def playSound(address: str, *args List[Any]):
    if !open:
        openAbleton()
    key = str(args[0])
    wait = args[1]
    p.keyDown(key)
    print(f"{key} pressed")
    sleep(wait)

sounds = [1,2,3,4]
songs = [5,6,7,8]

num_sounds = len(sounds)
num_songs = len(songs)


# openAbleton()
# p.confirm(text = 'Is Ableton Open?',buttons=['yes','cancel'])





