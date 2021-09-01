#!/usr/bin/python3


import pyautogui
import time

# .moveTo - moving the mouse to various x and y coordinates (0,0) is in top left (max_x, max_y) is in bottom right
# .click() does a left click action (this method can also take an x and y coordinate)
for _ in range(3):
    pyautogui.moveTo(600, 500, duration=0.5)
    pyautogui.click()
    time.sleep(3)
    # performing a right click
    pyautogui.rightClick()
    time.sleep(3)
    






