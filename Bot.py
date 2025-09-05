from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#https://humanbenchmark.com/tests/reactiontime
#X:  825 Y:  452 RGB: ( 75, 219, 106)

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(825, 452)[1] == 219:
        click()

    if pyautogui.pixelMatchesColor(825, 452, (75, 219, 106), tolerance=10):
        click()