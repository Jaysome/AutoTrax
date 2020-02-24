#!usr/bin/python3.7.4

__version__ = "1.7 Test 6"

import time
import sys
import ctypes
import os
import threading
# statement used for greenthumb confidence
# noinspection PyUnresolvedReferences
import cv2
import pyautogui

import Trax
import Automation
from Download import updatecheck

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


def main():
    fullauto = False
    Automation.demon_running = True
    demon = threading.Thread(target=Automation.login(), daemon=True)
    demon.start()
    while True:
        try:
            Trax.askforinputs()
            trax_inputs = Trax.trax_dict
            printinputconfirm(trax_inputs, 10, 11)
            print('Confirm entered values are correct? (Y/N)')
            confirm = input().strip().upper()
            if confirm == 'Y':
                print()
                print('Good Job!')
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
            Automation.demon_running = False
            demon.join()
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
    print('CONFIRM INPUTS'.center(left_width * 2 + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width) + '>'.center(left_width) + str(v).rjust(right_width))


ctypes.windll.kernel32.SetConsoleTitleW("autoTRAX " + __version__)
os.system("cls")
print("""
  █████╗ ██╗   ██╗████████╗ ██████╗ ████████╗██████╗  █████╗ ██╗  ██╗
 ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝
 ███████║██║   ██║   ██║   ██║   ██║   ██║   ██████╔╝███████║ ╚███╔╝ 
 ██╔══██║██║   ██║   ██║   ██║   ██║   ██║   ██╔══██╗██╔══██║ ██╔██╗ 
 ██║  ██║╚██████╔╝   ██║   ╚██████╔╝   ██║   ██║  ██║██║  ██║██╔╝ ██╗
 ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝""")
updatecheck(__version__)
main()
