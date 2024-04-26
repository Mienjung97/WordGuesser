import time
import os

# This file contains short functions that improve the game experience


def print_line():
    """
    Add 79 dashes to form a line
    """
    print("_" * 79, "\n")


def pause(u):
    """
    Function to delay print statements adn takes a float as delay
    in seconds.
    """
    time.sleep(u)


def paused_print_05(print_txt):
    """
    Combines the pause (0.5s) and print functions for readability.
    """
    print(print_txt)
    pause(0.5)


def paused_print_1(print_txt):
    """
    Combines the pause (1s) and print functions for readability.
    """
    print(print_txt)
    pause(1)


def paused_print_2(print_txt):
    """
    Combines the pause (2s) and print functions for readability.
    """
    print(print_txt)
    pause(2)


# https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
def cls():
    os.system("cls" if os.name == "nt" else "clear")
