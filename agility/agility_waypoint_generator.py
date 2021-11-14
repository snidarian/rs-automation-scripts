#!/usr/bin/python3

from pyautogui import _snapshot
import pynput
import csv
import time



# functions to trigger when keyboard keys are pressed for mouse is clicked
def on_click(x, y, button, pressed) -> None:
    if button.name == "left" and pressed == True:
        waypoint_time = (time.perf_counter() - start)
        waypoint_journey_list.append([x, y, button.name, waypoint_time])
        print(f"Left click at ({x}, {y} at {waypoint_time} seconds)")
        

    if button.name == "right" and pressed == True:
        waypoint_time = (time.perf_counter() - start)
        waypoint_journey_list.append([x, y, button.name, waypoint_time])
        print(f"Right click at ({x}, {y} at {waypoint_time} seconds)")
        


def on_press(key) -> None:
    # escape key stops the recording sequence for both listeners and freezes the current state of waypoint_journey_list array
    if key == pynput.keyboard.Key.esc:
        print("You pressed escape. Waypoint sequencing terminated..")
        mouse_listener.stop()
        # returning False stops the listener
        return False


    
    
# Set up two listener object threads, one for the mouse and one for the keyboard
keyboard_listener = pynput.keyboard.Listener(
    on_press=on_press,
)

mouse_listener = pynput.mouse.Listener(
    on_click=on_click,
)

def main() -> None:
    global start
    start = time.perf_counter()
    
    try:
        mouse_listener.start()
        keyboard_listener.start()
        while True:
            time.sleep(1)
        
    except KeyboardInterrupt:
        print("\nProgram terminated manually.")
        print(f"Journey waypoints: {waypoint_journey_list}")
        # For loop that transforms all duration values
        
        # This section will use the information stored in the waypoint_journey_list array to construct a csv of the waypoints
        with open(f"{task_name}.csv", mode='w') as taskfile_csv:
            taskfile_writer = csv.writer(taskfile_csv, delimiter=',')
            for entry in waypoint_journey_list:
                taskfile_writer.writerow([entry[0],entry[1],entry[2], entry[3]])
    stop = time.perf_counter()
    total = (stop - start)
    
    

if __name__ == "__main__":
    task_name = input("Enter a task name: ")
    waypoint_journey_list = []
    main()



















