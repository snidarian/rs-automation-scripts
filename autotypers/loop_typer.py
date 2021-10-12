#!/usr/bin/python3


import pyautogui
import random
import time

sentence_array = []


# How many sentences would you like to loop through
number_sentences = input("Number of sentences: ")
number_sentences = int(number_sentences)

# How many loops
loop_iterations = input("How many loops? ")
loop_iterations = int(loop_iterations)

# set delay - delay necessary to click on client before typing begins
delay = input("Set delay: ")
delay = int(delay)

for sentence in range(number_sentences):
    current_input_sentence = input(f"Sentence {(sentence + 1)}: ")
    sentence_array.append(current_input_sentence)
print(sentence_array)


time.sleep(delay)

def write_all_sentences(sentence_array):
    for sentence in sentence_array:
        pyautogui.write(f"{sentence}", interval=0.12)
        pyautogui.press('enter')
        time.sleep(0.8)


count = 0
while count <= (loop_iterations - 1):
    print(f"Loop {(count + 1)}")
    write_all_sentences(sentence_array)
    count+=1











