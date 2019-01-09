#! python3

import pyautogui
import time
import sys
import cv2

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

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
        print('TYPE: ', end='')  # TODO Modify name type is lame
        time.sleep(0.1)
        pyautogui.typewrite('INSP/CHK')
        inspchk = input()
        inspchk.strip()
        if len(inspchk) > 0:
            break
        print('INVALID.')
    inspchk = inspchk.upper()

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

    traxData = [name, date, hr, mn, station, inspchk, work, logpage]


    def printpicnic(items_dict, left_width, right_width):
        print('CONFIRM INPUTS'.center(left_width * 2 + right_width, '-'))
        for k, v in items_dict.items():
            print(k.ljust(left_width) + '>'.center(left_width) + str(v).rjust(right_width))


    traxDict = {'MECHANIC': name, 'DATE': date, 'HR:MN': hr + ':' + mn,
                'TYPE': inspchk, 'STATION': station, 'LOGPAGE': logpage}

    printpicnic(traxDict, 10, 10)

    print('Confirm entered values are correct? (Y/N)')
    confirm = input()
    confirm.strip()
    confirm = confirm.upper()
    if confirm == 'Y':
        print('Good Job')
        break

# TEST VALUES #
# name = 'JAY'
# date = '01/05/2019'
# hr = '12'
# mn = '00'
# inspchk = 'INSP/CHK'
# station = 'YUL'
# work = 'WORK ACCOMPLISHED AS PER TASK CARD INSTRUCTIONS.'
# logpage = '12345'
#############################################################

restartCondition = True


def clickntype(clicklocation, text):
    pyautogui.doubleClick(clicklocation)
    pyautogui.typewrite(text, interval=0.1)


def tabntype(numberoftabs, text):
    pyautogui.typewrite('\t' * numberoftabs)
    pyautogui.typewrite(text, interval=0.1)


def restarter():
    while True:
        print('\nRESTART AUTO TRAX ? (Y/N)')
        restart = input()
        restart.strip()
        restart = restart.upper()

        if restart == 'Y':
            print('\n\nRESTARTING AUTO TRAX...\nCTRL-C TO INTERRUPT')
            break
        if restart == 'N':
            print('\nGoodbye')
            time.sleep(1)
            sys.exit()


try:
    print('\n\nSTARTING AUTO TRAX...\nCTRL-C TO INTERRUPT')
    print('Choose Mode: coord or tab')
    mode = input()
    mode.strip()
    mode = mode.upper()

    if mode == 'COORD':
        # ------------Coordinate Mode---------- #
        while restartCondition:
            while True:
                coords = pyautogui.locateCenterOnScreen('saveIcon.png')
                if coords is not None:
                    x = coords[0]
                    y = coords[1]
                    break
                print('Cannot find an opened trax task card')

            statusLoc = (x + 160, y + 80)  # *OLD CORDS* X+150 Y+160
            byLoc = (x + 160, y + 127)  # x + 150, y + 205
            dateLoc = (x + 480, y + 193)  # x + 500, y + 270
            hrLoc = (x + 530, y + 193)  # x + 550, y + 270
            mnLoc = (x + 550, y + 193)  # x + 570, y + 270
            stationLoc = (x + 610, y + 193)  # x + 600, y + 270
            inspchkLoc = (x + 610, y + 170)  # tentative location
            workLoc = (x + 300, y + 300)  # x + 300, y + 380
            saveIconLoc = (x, y)  # x + 17, y + 80
            workTabLoc = (x + 480, y + 520)  # x + 500, y + 600
            logPageLoc = (x + 540, y + 30)  # x + 560, y + 105


            # TODO implement status behavior
            clickntype(byLoc, name)
            clickntype(dateLoc, date)
            clickntype(hrLoc, hr)
            clickntype(mnLoc, mn)
            clickntype(stationLoc, station)
            clickntype(inspchkLoc, inspchk)
            clickntype(workLoc, work)
            pyautogui.doubleClick(workTabLoc)
            time.sleep(2)
            clickntype(logPageLoc, logpage)

            print('AUTO TRAX COMPLETE')
            restarter()

    elif mode == 'TAB':
        # ----------------Tab Mode---------------- #
        while restartCondition:
            # tentative tab values
            statusToBy = 2
            byToInsp = 2
            inspToDate = 1
            dateToHr = 1
            hrToMn = 1
            mnToStation = 1
            stationToWork = 1
            workToLogpage = 6

            while True:
                coords = pyautogui.locateCenterOnScreen('status.png')
                if coords is not None:
                    break
                print('Cannot find an opened trax task card')
            # potential implementation of status
            # pyautogui.click(coords)
            # pyautogui.typewrite(['c','enter'], interval = 0.2)

            tabntype(statusToBy, name)
            tabntype(byToInsp, inspchk)
            tabntype(inspToDate, date)
            tabntype(dateToHr, hr)
            tabntype(hrToMn, mn)
            tabntype(mnToStation, station)
            tabntype(stationToWork, work)

            workCoords = pyautogui.locateCenterOnScreen('workAccomplished.png', confidence=0.8)
            pyautogui.click(workCoords)
            tabntype(workToLogpage, logpage)

            print('AUTO TRAX COMPLETE')
            restarter()

    # when ready to automate further#

    # saveCoords = pyautogui.locateCenterOnScreen('saveIcon.png')
    # pyautogui.click(saveCoords)
    # greenThumb= (385, 240)
    # pyautogui.moveRel(greenThumb)
    # pyautogui.click()
    # time.sleep(2)
    # pyautogui.click()

except KeyboardInterrupt:
    print('Interrupted')
