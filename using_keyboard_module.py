#!/usr/bin/python3



import time
from pynput.keyboard import Key,Controller



keyboard = Controller()

#keyboard.type("This is a test message using a keyboard object")

for _ in range(5):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)















