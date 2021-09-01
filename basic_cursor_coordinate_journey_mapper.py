#!/usr/bin/python3


import pyautogui
import pynput
import csv
import time


# functions to trigger when keyboard keys are pressed for mouse is clicked
def on_click(x, y, button, pressed) -> None:
    if button.name == "left" and pressed == True:
        print(f"Left click at ({x}, {y})")
        waypoint_journey_list.append([x, y, button.name])
        
    if button.name == "right" and pressed == True:
        print(f"Right click at ({x}, {y})")
        waypoint_journey_list.append([x, y, button.name])

def on_press(key) -> None:
    print(key)


# Set up two listener object threads, one for the mouse and one for the keyboard
keyboard_listener = pynput.keyboard.Listener(
    on_press=on_press,
)

mouse_listener = pynput.mouse.Listener(
    on_click=on_click,
)

def main() -> None:
    try:
        mouse_listener.start()
        keyboard_listener.start()
        while True:
            time.sleep(1)
        
    except KeyboardInterrupt:
        print("\nProgram terminated manually.")
        print(waypoint_journey_list)

    # This section will use the information stored in the waypoint_journey_list array to construct a csv of the waypoints


if __name__ == "__main__":
    waypoint_journey_list = []
    main()



















