#! python3

# Copyright 2019, Jérémi Morin, All rights reserved.
__version__ = "1.5.6 Beta"

import pyautogui
import time
import sys
import ctypes
# statement used for greenthumb confidence
# noinspection PyUnresolvedReferences
import cv2

import Inputs
import Automation

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


def main():
    while True:
        try:
            Inputs.askforinputs()
            trax_inputs = Inputs.askforinputs().trax_dict
            printinputconfirm(trax_inputs, 10, 11)
            print('Confirm entered values are correct? (Y/N)')
            confirm = input().strip().upper()
            if confirm == 'Y':
                print('\nGood Job!')
                break

        except KeyboardInterrupt:
            main()
            pass

    print('\nSTARTING autoTRAX...\nCTRL-C or move mouse top left to interrupt\n')

    while True:
        try:
            coords = Automation.lookfortaskcard()

            Automation.filltaskcard(coords[0], coords[1])

        except pyautogui.FailSafeException:
            print('\nautoTRAX paused by failsafe')
            pauseandrestart()
            pass

        except KeyboardInterrupt:
            print('\nautoTRAX paused by CTRL-C')
            pauseandrestart()
            pass


def pauseandrestart():
    print('\nY to restart autoTRAX ')
    print('NEW for a new aircraft')
    restart = input().strip().upper()
    if restart == 'Y':
        print('\n\nRESTARTING autoTRAX...\nCTRL-C or move mouse top left to interrupt\n')
    elif restart == 'NEW':
        main()
    elif restart == 'LOVE YOU':
        print('\nLove you too!')
        time.sleep(1)
        sys.exit()
    else:
        print('\nGoodbye')
        time.sleep(1)
        sys.exit()


def printinputconfirm(items_dict, left_width, right_width):
    print('CONFIRM INPUTS'.center(left_width * 2 + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width) + '>'.center(left_width) + str(v).rjust(right_width))


ctypes.windll.kernel32.SetConsoleTitleW("autoTRAX " + __version__)
print('Welcome to autoTRAX ' + __version__ + ', Enjoy!')
print('To get the latest version of autoTRAX go to bit.ly/skyautotrax')
main()
