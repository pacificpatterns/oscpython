import pyautogui as p 
from time import sleep


open = False

def openAbleton():
    p.keyDown("command")
    p.press('space')
    p.keyUp("command")
    p.write('ableton')
    p.press('enter')
    open = True

def playSound(key, wait):
    p.keyDown(str(key))
    sleep(wait)



# openAbleton()
# p.confirm(text = 'Is Ableton Open?',buttons=['yes','cancel'])





