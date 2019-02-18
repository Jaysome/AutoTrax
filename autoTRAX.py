#! python3

# Copyright 2019, Jérémi Morin, All rights reserved.

import pyautogui
import pywinauto.keyboard as kb
import time
import sys
import cv2

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

priority_user = {'JMORIN', 'DCHARTRA'}

while True:
    while True:
        print('MECHANIC: ', end='')
        name = input()
        name.strip()
        if name.isalpha():
            break
        print('INVALID. Name must be letters only otherwise it fucks everything')
    name = name.upper()

    while True:
        print('CLOSED ON (MM/DD/YYYY): ', end='')
        date = input()
        date.strip()
        month = int(date[0] + date[1])
        # ghetto security feature
        if month >= 3 and name not in priority_user:
            sys.exit()
        elif len(date) == 10 and month <= 12:
            break
        print('INVALID. Date must be in format MM/DD/YYYY')

    while True:
        print('ZULU TIME(HR:MN): ', end='')
        zulu = input()
        zulu.strip()
        hr = zulu[0] + zulu[1]
        mn = zulu[-2] + zulu[-1]
        if hr.isdecimal() is False:
            hr = '0' + hr[0]
        if mn.isdecimal() is False:
            mn = '0' + zulu[-1]
        if int(hr) < 24 and int(mn) < 60 and hr.isdecimal() and mn.isdecimal() and len(zulu) >= 4:
            break
        print('INVALID. Do it right this time')

    while True:
        print('STATION: ', end='')
        time.sleep(0.1)
        pyautogui.typewrite('YUL')
        station = input()
        station.strip()
        if station.isalpha() and len(station) == 3:
            break
        print('INVALID. Station must contain only 3 letters')
    station = station.upper()

    while True:
        print('RESOLUTION: ', end='')
        time.sleep(0.1)
        pyautogui.typewrite('INSP' + "/" + 'CHK')
        resolution = input()
        resolution.strip()
        if len(resolution) > 0:
            break
        print('INVALID.')
    resolution = resolution.upper()

    while True:
        print('LOGPAGE: ', end='')
        logpage = input()
        logpage.strip()
        if logpage.isdecimal():
            break
        print('INVALID. Logpage must be numbers only')

    traxData = [name, date, hr, mn, station, resolution, logpage]


    def printpicnic(items_dict, left_width, right_width):
        print('CONFIRM INPUTS'.center(left_width * 2 + right_width, '-'))
        for k, v in items_dict.items():
            print(k.ljust(left_width) + '>'.center(left_width) + str(v).rjust(right_width))


    traxDict = {'MECHANIC': name, 'DATE': date, 'HR:MN': hr + ':' + mn,
                'RESOLUTION': resolution, 'STATION': station, 'LOGPAGE': logpage}

    printpicnic(traxDict, 10, 10)

    print('Confirm entered values are correct? (Y/N)')
    confirm = input()
    confirm.strip()
    confirm = confirm.upper()
    if confirm == 'Y':
        print('\nGood Job!')
        break

# TEST VALUES #
# name = 'JAY'
# date = '01/05/2019'
# hr = '12'
# mn = '00'
# resolution = 'INSP/CHK'
# station = 'YUL'
# work = 'WORK ACCOMPLISHED AS PER TASK CARD INSTRUCTIONS.'
# logpage = '12345'
#############################################################

# not sure if useful
# statusToBy = 4
# byToRes = 1
# resToDate = 1
# dateToHr = 1
# hrToMn = 0
# mnToStation = 1
# stationToWork = 1
# workToLogpage = 3


def clickntype(clicklocation, text):
    pyautogui.click(clicklocation)
    pyautogui.typewrite(text)


def eraser():
    kb.SendKeys("{VK_DELETE 10}")


def eraserhotkey():
    kb.SendKeys('^+{RIGHT}')


def saver(savecoords):
    pyautogui.click(savecoords)
    # TODO loop greenthumb to give it more chance to find
    # tick = 0
    greenthumb = pyautogui.locateCenterOnScreen('greenThumb.png', confidence=0.8)
    pyautogui.click(greenthumb)
    time.sleep(1)
    pyautogui.click(greenthumb)


def restarter():
    print('\nRESTART autoTRAX ? (Y/N)')
    restart = input()
    restart.strip()
    restart = restart.upper()

    if restart == 'Y':
        print('\n\nRESTARTING autoTRAX...\nMOVE MOUSE TOP LEFT CORNER TO INTERRUPT')
    else:
        print('\nGoodbye')
        time.sleep(1)
        sys.exit()


print('\nSTARTING autoTRAX...\nMOVE MOUSE TOP LEFT CORNER TO INTERRUPT')
while True:
    try:
        helper = 0
        while True:
            statusLoc = pyautogui.locateCenterOnScreen('status.png')
            if statusLoc is not None:
                x = statusLoc[0]
                y = statusLoc[1]
                break
            statusLoc = pyautogui.locateCenterOnScreen('statusBlue.png')
            if statusLoc is not None:
                x = statusLoc[0]
                y = statusLoc[1]
                break
            helper += 1
            print('Looking for an opened trax task card...' + '(' + str(helper) + ')')

        saveLoc = (x - 141, y - 82)
        byLoc = (x + 0, y + 45)
        dateLoc = (x + 340, y + 113)
        hrLoc = (x + 388, y + 113)
        mnLoc = (x + 410, y + 113)
        stationLoc = (x + 470, y + 113)
        resolutionLoc = (x + 487, y + 78)
        workLoc = (x + 0, y + 220)
        workclickLoc = (x + 0, y + 315)
        workTabLoc = (x + 347, y + 437)
        logPageLoc = (x + 400, y - 56)

        pyautogui.click(statusLoc)
        pyautogui.typewrite('c')

        pyautogui.click(byLoc)
        eraserhotkey()
        pyautogui.typewrite(name)

        clickntype(dateLoc, date)
        clickntype(hrLoc, hr)
        clickntype(mnLoc, mn)

        pyautogui.click(stationLoc)
        eraserhotkey()
        pyautogui.typewrite(station)

        clickntype(resolutionLoc, resolution)

        pyautogui.doubleClick(workclickLoc)
        time.sleep(0.5)

        pyautogui.doubleClick(workTabLoc)
        time.sleep(0.5)
        clickntype(logPageLoc, logpage)

        print('autoTRAX COMPLETE')
        saver(saveLoc)

    except pyautogui.FailSafeException:
        print('autoTRAX paused by failsafe')
        restarter()
        pass

    except KeyboardInterrupt:
        print('autoTRAX paused by CTRL-C')
        restarter()
        pass



