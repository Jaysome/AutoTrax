#! python3

# Copyright 2019, Jérémi Morin, All rights reserved.
__version__ = "1.7 Test 3"

import pyautogui
import time
import sys
import ctypes
import os
# statement used for greenthumb confidence
# noinspection PyUnresolvedReferences
import cv2

import Trax
import Automation
from Download import updatecheck

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

c = {"RED": "\u001b[31m", "GREEN": "\u001b[32m", "YELLOW": "\u001b[33m", "BLUE": "\u001b[34m",
     "MAGENTA": "\u001b[35m", "CYAN": "\u001b[36m", "WHITE": "\u001b[37m", "RESET": "\u001b[0m",
     "BOLD": "\u001b[1m", "UNDERLINE": "\u001b[4m", "REVERSED": "\u001b[7m", "BLUEBACK": "\u001b[44m"}


def main():
    fullauto = False
    while True:
        try:
            Trax.askforinputs()
            trax_inputs = Trax.trax_dict
            printinputconfirm(trax_inputs, 10, 11)
            print('Confirm entered values are correct? (Y/N)')
            confirm = input().strip().upper()
            if confirm == 'Y':
                print(c["YELLOW"] + c["BOLD"])
                print(c["UNDERLINE"] + 'Good Job!' + c["RESET"])
                break
            elif confirm == 'FULL':
                fullauto = True
                print('\nSuper Secret mode activated!')
                time.sleep(1)
                break

        except KeyboardInterrupt:
            main()
            pass

    print('\nSTARTING autoTRAX...\nCTRL-C or move mouse top left to interrupt\n')

    while True:
        try:
            coords = Automation.lookfortaskcard(fullauto)

            Automation.filltaskcard(coords[0], coords[1])

        except pyautogui.FailSafeException:
            print('\nautoTRAX paused by failsafe')
            pauseandrestart()
            pass

        except KeyboardInterrupt:
            print('\nautoTRAX paused')
            pauseandrestart()
            pass


def pauseandrestart():
    print('\nY to restart autoTRAX ')
    print('NEW for a new aircraft')
    restart = input().strip().upper()
    if restart == 'Y':
        print('\nRESTARTING autoTRAX...\nCTRL-C or move mouse top left to interrupt\n')
    elif restart == 'NEW':
        main()
    elif restart == 'LOVE YOU':
        print('\nautoTRAX loves you too!')
        time.sleep(1)
        sys.exit()
    else:
        print('\nGoodbye')
        time.sleep(1)
        sys.exit()


def printinputconfirm(items_dict, left_width, right_width):
    print()
    print(c["BLUEBACK"] + 'CONFIRM INPUTS'.center(left_width * 2 + right_width, '-') + c["RESET"])
    for k, v in items_dict.items():
        print(c["BLUEBACK"] + k.ljust(left_width) + '>'.center(left_width) + str(v).rjust(right_width) + c["RESET"])


ctypes.windll.kernel32.SetConsoleTitleW("autoTRAX " + __version__)
os.system("cls")
print(c["GREEN"] + c["BOLD"] + """
  █████╗ ██╗   ██╗████████╗ ██████╗ ████████╗██████╗  █████╗ ██╗  ██╗
 ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝
 ███████║██║   ██║   ██║   ██║   ██║   ██║   ██████╔╝███████║ ╚███╔╝ 
 ██╔══██║██║   ██║   ██║   ██║   ██║   ██║   ██╔══██╗██╔══██║ ██╔██╗ 
 ██║  ██║╚██████╔╝   ██║   ╚██████╔╝   ██║   ██║  ██║██║  ██║██╔╝ ██╗
 ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝""" + c["RESET"])
updatecheck(__version__)
main()
