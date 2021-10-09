#!/usr/bin/python3


import pyautogui



start = pyautogui.locateCenterOnScreen('start.png', grayscale=False, confidence=0.7)


print(start)

pyautogui.moveTo(start)
pyautogui.leftClick()









