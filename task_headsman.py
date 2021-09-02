#!/usr/bin/python3

import argparse
import os
import pyautogui
import csv
import time
import random
from colorama import Fore


# Terminal color escape sequences
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
RESET = Fore.RESET


CURSOR_PATH_EFFECTS = [
    pyautogui.easeInBack,pyautogui.easeInBounce, pyautogui.easeInCirc,
    pyautogui.easeInCubic,pyautogui.easeInElastic,pyautogui.easeInExpo,
    pyautogui.easeInOutBack,pyautogui.easeInOutBounce,pyautogui.easeInOutCirc,
    pyautogui.easeInOutCubic,pyautogui.easeInOutElastic,pyautogui.easeInOutExpo,
    pyautogui.easeInOutQuad,pyautogui.easeInOutQuart,pyautogui.easeInOutQuint,
    pyautogui.easeInOutSine,pyautogui.easeInQuad,pyautogui.easeInQuart,
    pyautogui.easeInQuint,pyautogui.easeInSine,pyautogui.easeOutBack,
    pyautogui.easeOutBounce,pyautogui.easeOutCirc,pyautogui.easeOutCubic,
    pyautogui.easeOutElastic,pyautogui.easeOutExpo,pyautogui.easeOutQuad,
    pyautogui.easeOutQuart,pyautogui.easeOutQuint,pyautogui.easeInOutSine
]


def choose_random_cursor_path() -> object:
    effect = random.choice(CURSOR_PATH_EFFECTS)
    print(effect)
    type(effect)
    return effect


def main():
    # open a [task_name].csv file with csv library
    with open(f"{args.taskfile}", mode='r') as taskfile_csv:
        taskfile_reader = csv.reader(taskfile_csv, delimiter=',')
        # read all waypoint rows into python datastructure that exists outside of csv_reader file object
        for row in taskfile_reader:
            instruction_list.append([int(row[0]), int(row[1]), row[2]])
    # execute instructions found in the list
    for instruction in instruction_list:
        # Variables to create variation in xy coordiantes and time between actions
        time.sleep(random.uniform(0.0, 0.4))
        xnoise = random.randint(-2, +2)
        ynoise = random.randint(-2, +2)
        
        if instruction[2] == 'left':
            pyautogui.leftClick((instruction[0]+xnoise), (instruction[1]+ynoise), duration=duration, tween=choose_random_cursor_path())
        if instruction[2] == 'right':
            pyautogui.rightClick((instruction[0]+xnoise), (instruction[1]+ynoise), duration=duration, tween=choose_random_cursor_path())
        if instruction[2] == 'space':
            print("Space bar needs to be pressed")
            pyautogui.press('space')
    # clear the instructions_list methods
    instruction_list.clear()
        

if __name__ == "__main__":
    # setup argparse
    parser = argparse.ArgumentParser(description="Program takes taskname.csv and executes cursor clicks and keypresses")
    args = parser.add_argument("taskfile", help="taskfile.csv in CWD")
    args = parser.parse_args()
    # csv taskfile instruction data written into this python array
    instruction_list = []
    duration = input("Duration between clicks and keypresses: ")
    # Turn from string into integer
    duration = float(duration)
    loop = input("looping? (y/n) ")
    if loop.upper() == 'Y':
        loop = True
    elif loop.upper() == 'N':
        loop = False
    # IF loop evalutates to true:
    if loop == True:
        between_loops = input("Time between loops? ")
        between_loops = int(between_loops)
        loop_iterations = input("Number of loop iterations: ")
        loop_iterations = int(loop_iterations)
    # Display system datetime before process begins
    os.system('date')
    # If task loop requested, run for X number of iterations
    if loop == True:
        for _ in range(1, (loop_iterations + 1), 1):
            print(f"Starting task loop iteration {RED}{_}{RESET}/{loop_iterations}")
            main()
            # a tiny little bit of random interval noise between loops
            time.sleep((between_loops + random.randint(0, 2)))
    else:
        main()







