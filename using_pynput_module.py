#!/usr/bin/python3


import pynput


def on_click(x, y, button, pressed) -> None:
    print(x)
    print(y)
    if button.name == "left" and pressed == True:
        print("you clicked left")
    if button.name == "right" and pressed == True:
        print("you clicked right")
    print(pressed)


with pynput.mouse.Listener(
    on_click=on_click,
    
) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\nProgram terminated manually.")