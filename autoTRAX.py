#! python3

# Copyright 2019, Jérémi Morin, All rights reserved.
__version__ = "1.5.3"

import pyautogui
import pywinauto.keyboard as kb
import time
import sys
import ctypes
import random
import datetime
import os
# statement used for greenthumb confidence
# noinspection PyUnresolvedReferences
import cv2

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

team_one = ['JMORIN', 'AWESTWOO', 'DCHARTRA', 'GLAURIN', 'GPAQUIN', 'GVALLEE', 'JGRENON',
            'JLABERGE', 'KFEKKAR', 'MCOUTURE', 'MOUELLET', 'MPOIRIER', 'MROUTHIE', 'NKJONES',
            'PSIMARD', 'SFRICOTT']
team_snake = ['CGAGNON', 'EBROOKER', 'FLANGLOI', 'JRICHARD', 'LDOBSON', 'NTHIVIER', 'RLEROUX',
              'SDERY', 'SROY', 'SSTPIERR', 'XWANG', 'ZDEJANOV']
team_calvin = 'CBOYCE'


def main():
    while True:
        try:
            while True:
                print('\nMECHANIC: ', end='')
                name = input().strip().upper()
                if name.isalpha() and len(name) <= 8:
                    break
                print('INVALID! Name must be exactly like in trax otherwise it fucks everything')

            checknprintwithadjective(name)

            while True:
                print('CLOSED ON (MM/DD/YYYY): ', end='')
                now = datetime.datetime.utcnow()
                time.sleep(0.1)
                pyautogui.typewrite(now.strftime("%m/%d/%Y"))
                date = input().strip()
                if len(date) == 10:
                    full_date = fulldate(date)
                    if month <= 12:
                        break
                print('INVALID! Date must be in format MM/DD/YYYY')

            while True:
                print('ZULU TIME(HR:MN): ', end='')
                zulu = input().strip()
                if len(zulu) == 4 or len(zulu) == 5:
                    hr = zulu[0] + zulu[1]
                    mn = zulu[-2] + zulu[-1]
                    if hr.isdecimal() is False:
                        hr = '0' + zulu[0]
                    if mn.isdecimal() is False:
                        mn = '0' + zulu[-1]
                    if hr.isdecimal() and mn.isdecimal() and int(hr) < 24 and int(mn) < 60:
                        break
                print('INVALID! Only HR:MN and HRMN format is accepted')

            while True:
                print('STATION: ', end='')
                time.sleep(0.1)
                pyautogui.typewrite('YUL')
                station = input().strip().upper()
                if station.isalpha() and len(station) == 3:
                    break
                print('INVALID! Station must contain only 3 letters')

            while True:
                print('RESOLUTION: ', end='')
                time.sleep(0.1)
                pyautogui.typewrite('INSP' + "/" + 'CHK')
                resolution = input().strip().upper()
                if len(resolution) > 0:
                    break
                print('INVALID!')

            while True:
                print('LOGPAGE: ', end='')
                logpage = input().strip()
                if logpage:
                    first = logpage[0]
                    if logpage.isdecimal() or first == 'f' or first == 'F':
                        break
                print('INVALID logpage format')

            trax_dict = {'MECHANIC': name, 'DATE': full_date, 'HR:MN': hr + ':' + mn,
                         'RESOLUTION': resolution, 'STATION': station, 'LOGPAGE': logpage}

            printinputconfirm(trax_dict, 10, 11)

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
            helper = 0
            while True:
                status_loc = pyautogui.locateCenterOnScreen(resource_path('img\\status.png'),
                                                            grayscale=True)
                if status_loc is not None:
                    break
                status_loc = pyautogui.locateCenterOnScreen(resource_path('img\\statusBlue.png'),
                                                            grayscale=True)
                if status_loc is not None:
                    break
                status_loc = pyautogui.locateCenterOnScreen(resource_path('img\\statusWhite.png'),
                                                            grayscale=True)
                if status_loc is not None:
                    break
                helper += 1
                print('Looking for an opened trax task card...' + '(' + str(helper) + ')', end='\r')

            x = status_loc[0]
            y = status_loc[1]

            save_loc = (x - 141, y - 82)
            by_loc = (x + 0, y + 45)
            date_loc = (x + 340, y + 113)
            hr_loc = (x + 388, y + 113)
            mn_loc = (x + 410, y + 113)
            station_loc = (x + 470, y + 113)
            resolution_loc = (x + 487, y + 78)
            workclick_loc = (x + 0, y + 315)
            work_tab_loc = (x + 347, y + 437)
            log_page_loc = (x + 400, y - 56)
            # work_loc = (x + 0, y + 220)

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

            savetaskcard(save_loc)
            print('\nautoTRAX COMPLETE')

        except pyautogui.FailSafeException:
            print('\nautoTRAX paused by failsafe')
            pauseandrestart()
            pass

        except KeyboardInterrupt:
            print('\nautoTRAX paused by CTRL-C')
            pauseandrestart()
            pass


def printinputconfirm(items_dict, left_width, right_width):
    print('CONFIRM INPUTS'.center(left_width * 2 + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width) + '>'.center(left_width) + str(v).rjust(right_width))


def clickntype(clicklocation, text):
    pyautogui.click(clicklocation)
    pyautogui.typewrite(text)


def eraser():
    kb.SendKeys("{VK_DELETE 10}")


def eraserhotkey():
    kb.SendKeys('^+{RIGHT}')


def savetaskcard(savecoords):
    pyautogui.click(savecoords)
    greenthumb = None
    tick = 0
    while greenthumb is None:
        greenthumb = pyautogui.locateCenterOnScreen(resource_path('img\\greenThumb.png'),
                                                    confidence=0.8, grayscale=True)
        tick += 1
        if tick > 5:
            break
    pyautogui.click(greenthumb)
    time.sleep(1)
    pyautogui.click(greenthumb)


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


def fulldate(date):
    global month
    months_dict = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL',
                   8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}
    month = int(date[0] + date[1])
    day = int(date[3] + date[4])
    year = int(date[6] + date[7] + date[8] + date[9])

    return str(day) + ' ' + months_dict.get(month) + ' ' + str(year)


# gets absolute path for dev and pyinstaller
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def checknprintwithadjective(name):
    team_one_adjectives = random.choice(
        ['a brilliant', 'a celebrated', 'a distinguished', 'a fabulous', 'a glorious',
         'a legendary', 'a noble', 'a phenomenal', 'a prodigious', 'a quality', 'a remarkable',
         'a renowned', 'a revered', 'a splendid', 'a stupendous', 'a sublime', 'a superior',
         'a venerated', 'a wonderful', 'an amazing', 'an eminent', 'an esteemed', 'an exalted',
         'an excellent', 'an exceptional', 'an extraordinary', 'an honored', 'an illustrious',
         'an outstanding', 'a sexy', 'an admirable', 'a commendable', 'an honorable', 'a model',
         'a valuable', 'a great', 'a worthy', 'a solid', 'an exemplary', 'an invaluable',
         'an intrepid', 'a fearless', 'a gallant', 'a valiant', 'a valorous', 'an heroic', 'a bold',
         'a chivalrous', 'a stalwart', 'a powerful', 'an impressive', 'an energetic', 'a dynamic',
         'an influential', 'a mighty', 'a competent', 'a charismatic', 'an intense', 'an important',
         'a foremost'])
    team_snake_adjectives = random.choice(
        ['a', 'a good enough', 'a passable', 'a permitted', 'a satisfactory', 'a sufficient',
         'a suitable', 'a valid', 'a worthy', 'an acceptable', 'an accepted', 'an adequate',
         'an admissible', 'an all right', 'an allowable', 'an allowed', 'an approved',
         'an authorized', 'a fair enough', 'a capable'])

    if name in team_one:
        print('You are ' + team_one_adjectives + ' member of Team One.')
    elif name in team_snake:
        print('You are ' + team_snake_adjectives + ' member of Team Snake.')
    elif name in team_calvin:
        print('You are an approved user.')
    else:
        print('You are not an approved user! Please contact your system administrator.')
        time.sleep(2)
        sys.exit()


ctypes.windll.kernel32.SetConsoleTitleW("autoTRAX " + __version__)
print('Welcome to autoTRAX ' + __version__ + ', Enjoy!')
print('To get the latest version of autoTRAX go to bit.ly/skyautotrax')
main()
