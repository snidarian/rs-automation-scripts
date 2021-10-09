#!/usr/bin/python3

import time
import random
import pyautogui
from colorama import Fore


red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Fore.RESET

count = 1
display_header = True
while count < 12:
    
    # Try to recognize green obstacle
    nextobstacle = pyautogui.locateCenterOnScreen(f'green_clickboxes/g{count}.png', grayscale=True, confidence=0.7)
    # if the try to recognize green obstacle fails, then try to recognize red obstacle.
    if nextobstacle == None:
        print(f"{red}F{reset}")
        #nextobstacle = pyautogui.locateCenterOnScreen(f'red_clickboxes/r{count}.png', grayscale=False, confidence=0.8)
        time.sleep(.05)
    else:
        print(f"\n{green}Success{reset}")
        pyautogui.moveTo(nextobstacle, duration=random.randint(2, 3))
        pyautogui.leftClick()
        display_header = True
        count+=1
        time.sleep(5)

        
        
    
    
    








