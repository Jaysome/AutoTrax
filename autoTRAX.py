#! python3

# Copyright 2019, Jérémi Morin, All rights reserved.

import pyautogui
import pywinauto.keyboard as kb
import time
import sys
import os.path
import cv2

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

priority_user = {'JMORIN', 'DCHARTRA', 'NKJONES', 'MROUTHIE'}
GHETTO_SECURITY = 5


def main():
    while True:
        while True:
            print('MECHANIC: ', end='')
            name = input().strip().upper()
            if name.isalpha() and len(name) <= 8:
                break
            print('INVALID. Name must be exactly like in trax otherwise it fucks everything')

        while True:
            print('CLOSED ON (MM/DD/YYYY): ', end='')
            date = input().strip()
            month = int(date[0] + date[1])
            if len(date) == 10 and month <= 12:
                break
            print('INVALID. Date must be in format MM/DD/YYYY')

        # Ghetto Security Feature
        if month >= GHETTO_SECURITY and name not in priority_user:
            sys.exit()

        while True:
            print('ZULU TIME(HR:MN): ', end='')
            zulu = input().strip()
            hr = zulu[0] + zulu[1]
            mn = zulu[-2] + zulu[-1]
            if hr.isdecimal() is False:
                hr = '0' + hr[0]
            if mn.isdecimal() is False:
                mn = '0' + zulu[-1]
            if int(hr) < 24 and int(mn) < 60 and hr.isdecimal() and mn.isdecimal() and len(
                    zulu) >= 4:
                break
            print('INVALID. Do it right this time')

        while True:
            print('STATION: ', end='')
            time.sleep(0.1)
            pyautogui.typewrite('YUL')
            station = input().strip().upper()
            if station.isalpha() and len(station) == 3:
                break
            print('INVALID. Station must contain only 3 letters')

        while True:
            print('RESOLUTION: ', end='')
            time.sleep(0.1)
            pyautogui.typewrite('INSP' + "/" + 'CHK')
            resolution = input().strip().upper()
            if len(resolution) > 0:
                break
            print('INVALID.')

        while True:
            print('LOGPAGE: ', end='')
            logpage = input().strip()
            if logpage.isdecimal():
                break
            print('INVALID. Logpage must be numbers only')

        trax_data = [name, date, hr, mn, station, resolution, logpage]

        def printpicnic(items_dict, left_width, right_width):
            print('CONFIRM INPUTS'.center(left_width * 2 + right_width, '-'))
            for k, v in items_dict.items():
                print(k.ljust(left_width) + '>'.center(left_width) + str(v).rjust(right_width))

        trax_dict = {'MECHANIC': name, 'DATE': date, 'HR:MN': hr + ':' + mn,
                     'RESOLUTION': resolution, 'STATION': station, 'LOGPAGE': logpage}

        printpicnic(trax_dict, 10, 10)

        print('Confirm entered values are correct? (Y/N)')
        confirm = input().strip().upper()
        if confirm == 'Y':
            print('\nGood Job!')
            break

    print('\nSTARTING autoTRAX...\nCTRL-C or move mouse top left to interrupt')

    while True:
        try:
            helper = 0
            while True:
                status_loc = pyautogui.locateCenterOnScreen('status.png')
                if status_loc is not None:
                    x = status_loc[0]
                    y = status_loc[1]
                    break
                status_loc = pyautogui.locateCenterOnScreen('statusBlue.png')
                if status_loc is not None:
                    x = status_loc[0]
                    y = status_loc[1]
                    break
                helper += 1
                print('Looking for an opened trax task card...' + '(' + str(helper) + ')')

            save_loc = (x - 141, y - 82)
            by_loc = (x + 0, y + 45)
            date_loc = (x + 340, y + 113)
            hr_loc = (x + 388, y + 113)
            mn_loc = (x + 410, y + 113)
            station_loc = (x + 470, y + 113)
            resolution_loc = (x + 487, y + 78)
            work_loc = (x + 0, y + 220)
            workclick_loc = (x + 0, y + 315)
            work_tab_loc = (x + 347, y + 437)
            log_page_loc = (x + 400, y - 56)

            pyautogui.click(status_loc)
            pyautogui.typewrite('c')

            pyautogui.click(by_loc)
            eraserhotkey()
            pyautogui.typewrite(name)

            clickntype(date_loc, date)
            clickntype(hr_loc, hr)
            clickntype(mn_loc, mn)

            pyautogui.click(station_loc)
            eraserhotkey()
            pyautogui.typewrite(station)

            clickntype(resolution_loc, resolution)

            pyautogui.doubleClick(workclick_loc)
            time.sleep(0.5)

            pyautogui.doubleClick(work_tab_loc)
            time.sleep(0.5)
            clickntype(log_page_loc, logpage)

            saver(save_loc)
            print('autoTRAX COMPLETE')

        except pyautogui.FailSafeException:
            print('autoTRAX paused by failsafe')
            restarter()
            pass

        except KeyboardInterrupt:
            print('autoTRAX paused by CTRL-C')
            restarter()
            pass


def clickntype(clicklocation, text):
    pyautogui.click(clicklocation)
    pyautogui.typewrite(text)


def eraser():
    kb.SendKeys("{VK_DELETE 10}")


def eraserhotkey():
    kb.SendKeys('^+{RIGHT}')


def saver(savecoords):
    pyautogui.click(savecoords)
    greenthumb = None
    tick = 0
    while greenthumb is None:
        greenthumb = pyautogui.locateCenterOnScreen('greenThumb.png', confidence=0.8)
        tick += 1
        if tick > 5:
            break
    pyautogui.click(greenthumb)
    time.sleep(1)
    pyautogui.click(greenthumb)


def restarter():
    print('\nY to restart autoTRAX ')
    print('NEW for a new aircraft', end='')
    if os.path.isfile('max.txt'):
        print(' (juste pour toi max)')
    restart = input().strip().upper()

    if restart == 'Y':
        print('\n\nRESTARTING autoTRAX...\nCTRL-C or move mouse top left to interrupt')
    elif restart == 'NEW':
        main()
    else:
        print('\nGoodbye')
        time.sleep(1)
        sys.exit()


main()
