import pyautogui
from random import randint
from time import sleep
from playsound3 import playsound
import os

pyautogui.FAILSAFE = True
path = os.path.dirname(os.path.abspath(__file__))
sound = os.path.join(path, "alarm.mp3")
clicks = input("Clicks (Y/N)? ").lower()

try:
    while True:
        #Numbers can switch depending on what you want to do and screen size
        x = randint(200, 1200)
        y = randint(200, 650)
        if clicks == "y":
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        pyautogui.moveTo(x, y, 0.5)
        sleep(2)

except pyautogui.FailSafeException:
    playsound(sound)

    print("The bot has stopped!")
