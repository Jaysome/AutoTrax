#! python3

import pyautogui
import pywinauto.keyboard as kb
import time
import sys
import cv2

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

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
        if len(date) == 10 and int(date[0] + date[1]) <= 12:
            break
        print('INVALID. Date must be in format MM/DD/YYYY')

    while True:
        print('HOUR(UTC): ', end='')
        hr = input()
        hr.strip()
        if hr.isdecimal() and len(hr) == 2:
            break
        print('INVALID. Time must contain only 2 numbers')

    while True:
        print('MINUTE(UTC): ', end='')
        mn = input()
        mn.strip()
        if mn.isdecimal() and len(mn) == 2:
            break
        print('INVALID. Time must contain only 2 numbers')

    while True:
        print('STATION: ', end='')
        station = input()
        station.strip()
        if station.isalpha() and len(station) == 3:
            break
        print('INVALID. Station must contain only 3 letters')
    station = station.upper()

    while True:
        print('RESOLUTION: ', end='')
        time.sleep(0.1)
        pyautogui.typewrite('INSP' + '/' + 'CHK')
        resolution = input()
        resolution.strip()
        if len(resolution) > 0:
            break
        print('INVALID.')
    resolution = resolution.upper()

    print('WORK ACCOMPLISHED: ', end='')
    time.sleep(0.1)
    pyautogui.typewrite('WORK ACCOMPLISHED AS PER TASK CARD INSTRUCTIONS.')
    work = input()
    work.strip()
    work = work.upper()

    while True:
        print('LOGPAGE: ', end='')
        logpage = input()
        logpage.strip()
        if logpage.isdecimal():
            break
        print('INVALID. Logpage must be numbers only')

    traxData = [name, date, hr, mn, station, resolution, work, logpage]


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
        print('Good Job!')
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

restartCondition = True

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


# TODO oublie pas que tu as enable le autosave apres la v0.4
def saver(savecoords):
    pyautogui.click(savecoords)
    greenthumb = (385, 240)
    pyautogui.moveRel(greenthumb)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()


def restarter():
    while True:
        print('\nRESTART AUTO TRAX ? (Y/N)')
        restart = input()
        restart.strip()
        restart = restart.upper()

        if restart == 'Y':
            print('\n\nRESTARTING AUTO TRAX...\n\nMOVE MOUSE TOP LEFT CORNER TO INTERRUPT')
            break
        if restart == 'N':
            print('\nGoodbye')
            time.sleep(1)
            sys.exit()


try:
    print('\n\nSTARTING AUTO TRAX...\n\nMOVE MOUSE TOP LEFT CORNER TO INTERRUPT')

    while restartCondition:
        helper = 0
        while True:
            coords = pyautogui.locateCenterOnScreen('saveIcon.png')
            if coords is not None:
                x = coords[0]
                y = coords[1]
                break
            helper += 1
            if helper == 5:
                print('Looking for an opened trax task card...')
                helper = 0

        statusLoc = (x + 160, y + 80)
        byLoc = (x + 160, y + 127)
        dateLoc = (x + 480, y + 193)
        hrLoc = (x + 530, y + 193)
        mnLoc = (x + 550, y + 193)
        stationLoc = (x + 610, y + 193)
        resolutionLoc = (x + 610, y + 158)
        workLoc = (x + 300, y + 300)
        workclickLoc = (x + 120, y + 390)
        workTabLoc = (x + 480, y + 520)
        logPageLoc = (x + 540, y + 30)

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

        print('AUTO TRAX COMPLETE')
        saver(coords)

# TODO allow restarting after interruption (look into signals or exception handling
        # restarter()

except KeyboardInterrupt:
    print('Interrupted')
    time.sleep(5)
    sys.exit()


