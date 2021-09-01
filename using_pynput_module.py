#!/usr/bin/python3


import pynput


def on_click(x, y, button, pressed) -> None:
    print(x)
    print(y)
    print(button)
    print(pressed)


with pynput.mouse.Listener(
    on_click=on_click,
    
) as listener:
    listener.join()
