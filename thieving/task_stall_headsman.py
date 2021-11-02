#!/usr/bin/python3

import argparse
import os
import pyautogui
import csv
import time
import random
from colorama import Fore



SCREEN_RESOLUTION = pyautogui.size()


# Terminal color escape sequences
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET


CURSOR_PATH_EFFECTS = [
    pyautogui.easeInQuad,
    pyautogui.easeOutQuad,
    pyautogui.easeInOutQuad
]


def choose_random_cursor_tween() -> object:
    effect = random.choice(CURSOR_PATH_EFFECTS)
    return effect

def skew_perfect_midpoints(x_mid, y_mid) -> int:
    # skewing amount calculated randomly - This number is really important for skewing the midpoint
    skew_factor = random.randint(1, 152000)
    # chooses which way to skew
    flip_flop = random.choice([True, False])
    # make sure the ratios are correct - +30 would have a greater impact on Y than on X in 3880X1080 resolution
    # divide each by the other
    if flip_flop == True:
        skewed_x = (x_mid + (skew_factor // SCREEN_RESOLUTION[1]))
        skewed_y = (y_mid - (skew_factor) // SCREEN_RESOLUTION[0])
    else:
        skewed_x = (x_mid - ((skew_factor // SCREEN_RESOLUTION[1])))
        skewed_y = (y_mid + ((skew_factor) // SCREEN_RESOLUTION[0]))
    return skewed_x, skewed_y


def main():
    # open a [task_name].csv file with csv library
    with open(f"{args.taskfile}", mode='r') as taskfile_csv:
        taskfile_reader = csv.reader(taskfile_csv, delimiter=',')
        # read all waypoint rows into python datastructure that exists outside of csv_reader file object
        for row in taskfile_reader:
            instruction_list.append([int(row[0]), int(row[1]), row[2]])
    # execute instructions found in the list
    for instruction in instruction_list:
        # values read from .csv are set to more understandable variable names
        x_destination = instruction[0]
        y_destination = instruction[1]
        command_action = instruction[2]
        # Variables to create variation in xy click destination coordiantes and time between actions
        time.sleep(random.uniform(0.0, 0.4))
        xnoise = random.randint(-3, +3)
        ynoise = random.randint(-3, +3)
        # When a mouse coordinate is determined half of the duration variable will be spend travelling to a SKEWED/OFFCENTER midpoint of the destination
        # 1. Calculate current mouse xy coordinates
        x_origin, y_origin = pyautogui.position()
        # 2. Calculate exact midpoint (The absolute values of the differences of the origin and destination xs and ys)
        x_midpoint, y_midpoint = abs((x_origin + x_destination) // 2), abs((y_origin + y_destination) // 2)
        # 3. Skew that midpoint to one side
        x_midpoint_skewed, y_midpoint_skewed = skew_perfect_midpoints(x_midpoint, y_midpoint)
        # 4. Reach skewed midpoint with cursor using .moveTo() method and duration=(duration/2)
        pyautogui.moveTo(x_midpoint_skewed, y_midpoint_skewed, duration=(duration/2))
        # The remainder of the journey (ie from the midpoint will be travelled with the either of these methods)
        if command_action == 'left':
            pyautogui.leftClick((x_destination+xnoise), (y_destination+ynoise), duration=(duration/2))
        if command_action == 'right':
            pyautogui.rightClick((x_destination+xnoise), (y_destination+ynoise), duration=(duration/2))
        if command_action == 'space':
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
    # Display system datetime before process begins - Print statements before/after control color for os.system
    print(YELLOW)
    os.system('date')
    print(RESET)
    # If task loop requested, run for X number of iterations
    if loop == True:
        for _ in range(1, (loop_iterations + 1), 1):
            print(f"Starting task loop iteration {GREEN}{_}{RESET}/{loop_iterations}")
            main()
            # a tiny little bit of random interval noise between loops
            time.sleep((between_loops + random.randint(0, 2)))
    else:
        main()







