#! python3

import pyautogui
import time
import sys
import cv2

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

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
        pyautogui.typewrite('INSP'+'/'+'CHK')
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
        print('Good Job')
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


def clickntype(clicklocation, text, backspaces):
    pyautogui.doubleClick(clicklocation)
    pyautogui.typewrite('\b' * backspaces)
    pyautogui.typewrite(text, interval=0.1)


def tabntype(numberoftabs, text, backspaces):
    pyautogui.typewrite('\t' * numberoftabs)
    pyautogui.typewrite('\b' * backspaces)
    pyautogui.typewrite(text, interval=0.1)


def statusimplem(coordinatesofstatus):
    pyautogui.click(coordinatesofstatus)
    pyautogui.typewrite('c')


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
            # TODO fix status bug +80 a lautre bout du monde +100 a coter
            statusLoc = (x + 160, y + 80)  # *OLD CORDS* X+150 Y+160
            byLoc = (x + 160, y + 127)  # x + 150, y + 205
            dateLoc = (x + 480, y + 193)  # x + 500, y + 270
            hrLoc = (x + 530, y + 193)  # x + 550, y + 270
            mnLoc = (x + 550, y + 193)  # x + 570, y + 270
            stationLoc = (x + 610, y + 193)  # x + 600, y + 270
            resolutionLoc = (x + 610, y + 158)
            workLoc = (x + 300, y + 300)  # x + 300, y + 380
            saveIconLoc = (x, y)  # x + 17, y + 80
            workTabLoc = (x + 480, y + 520)  # x + 500, y + 600
            logPageLoc = (x + 540, y + 30)  # x + 560, y + 105

            pyautogui.doubleClick(statusLoc)
            pyautogui.typewrite('c')
            clickntype(byLoc, name, 10)
            clickntype(dateLoc, date, 0)
            clickntype(hrLoc, hr, 0)
            clickntype(mnLoc, mn, 0)
            clickntype(stationLoc, station, 5)
            clickntype(resolutionLoc, resolution, 0)
            clickntype(workLoc, work, 0)
            pyautogui.doubleClick(workTabLoc)
            time.sleep(2)
            clickntype(logPageLoc, logpage, 0)

            print('AUTO TRAX COMPLETE')
            restarter()

    elif mode == 'TAB':
        # ----------------Tab Mode---------------- #
        while restartCondition:
            # tentative tab values
            statusToBy = 4
            byToRes = 1
            resToDate = 1
            dateToHr = 1
            hrToMn = 0
            mnToStation = 1
            stationToWork = 1
            workToLogpage = 3

            while True:
                coords = pyautogui.locateCenterOnScreen('status.png')
                if coords is not None:
                    break
                print('Cannot find an opened trax task card')

            #statusimplem(coords)
            pyautogui.doubleClick(coords)
            pyautogui.typewrite('c')
            tabntype(statusToBy, name, 10)
            tabntype(byToRes, resolution, 0)
            tabntype(resToDate, date, 0)
            tabntype(dateToHr, hr, 0)
            tabntype(hrToMn, mn, 0)
            tabntype(mnToStation, station, 5)
            tabntype(stationToWork, work, 0)

            workCoords = pyautogui.locateCenterOnScreen('workAccomplished.png', confidence=0.9)
            pyautogui.click(workCoords)
            tabntype(workToLogpage, logpage, 0)

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
