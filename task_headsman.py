#!/usr/bin/python3

import argparse
import os
import pyautogui
import csv
import time
import random


def main():
    # open a [task_name].csv file with csv library
    with open(f"{args.taskfile}", mode='r') as taskfile_csv:
        taskfile_reader = csv.reader(taskfile_csv, delimiter=',')
        # read all waypoint rows into python datastructure that exists outside of csv_reader file object
        for row in taskfile_reader:
            instruction_list.append([int(row[0]), int(row[1]), row[2]])
    # execute instructions found in the list
    for instruction in instruction_list:
        if instruction[2] == 'left':
            pyautogui.leftClick(instruction[0], instruction[1], duration=duration)
        if instruction[2] == 'right':
            pyautogui.rightClick(instruction[0], instruction[1], duration=duration)
        if instruction[2] == 'space':
            print("Space bar needs to be pressed")
            pyautogui.press('space')
        

if __name__ == "__main__":
    # setup argparse
    parser = argparse.ArgumentParser(description="Program takes taskname.csv and executes cursor clicks and keypresses")
    args = parser.add_argument("taskfile", help="taskfile.csv in CWD")
    args = parser.parse_args()
    instruction_list = []
    duration = input("Duration between actions: ")
    loop = input("looping? y/n")
    if loop.upper == 'Y':
        loop = True
    elif loop.upper == 'N':
        loop = False
    between_loops = input("Time between loops? ")
    between_loops = int(between_loops)
    loop_iterations = input("Number of loop iterations: ")
    loop_iterations = int(loop_iterations)
    duration = int(duration)
    if loop == True:
        for _ in range(loop_iterations):
            main()
            # a tiny little bit of random interval noise between loops
            time.sleep((between_loops + random.randint(0, 2)))
    else:
        main()







