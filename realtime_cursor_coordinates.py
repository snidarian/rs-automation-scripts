#!/usr/bin/python3


import pyautogui
import time
import os


# main loop displays mouse cursor coordinates in real time
def main():
    try:
        while True:
            xy_cursor_coordinates = pyautogui.position()
            print(xy_cursor_coordinates)
            time.sleep(0.1)
            os.system('clear')
    except KeyboardInterrupt:
        print("\nprogram terminated")



if __name__ == "__main__":
    main()




