from datetime import datetime
import random
import sys
import time

# fucked for a while as per https://github.com/pywinauto/pywinauto/issues/868
# import pywinauto.keyboard as kb
import pyautogui

import Teams

c = {"RED": "\u001b[31m", "GREEN": "\u001b[32m", "YELLOW": "\u001b[33m", "BLUE": "\u001b[34m",
     "MAGENTA": "\u001b[35m", "CYAN": "\u001b[36m", "WHITE": "\u001b[37m", "RESET": "\u001b[0m",
     "BOLD": "\u001b[1m", "UNDERLINE": "\u001b[4m", "REVERSED": "\u001b[7m", "BLUEBACK": "\u001b[44m"}

name = str
date = str
hr = int
mn = int
station = str
resolution = str
logpage = str
trax_dict = dict


def askforinputs():
    global name, date, hr, mn, station, resolution, logpage, trax_dict

    while True:
        print(c["RED"] + '\nMECHANIC: ' + c["RESET"], end='')
        name = input().strip().upper()
        if name.isalpha() and len(name) <= 8:
            break
        print('INVALID! Name must be exactly like in trax otherwise it fucks everything')

    Teams.validate(name)

    while True:
        print(c["RED"] + 'CLOSED ON (MM/DD/YYYY): ' + c["RESET"], end='')
        now = datetime.utcnow()
        time.sleep(0.1)
        # kb.SendKeys(now.strftime("%m/%d/%Y"), pause=0)
        pyautogui.write(now.strftime("%m/%d/%Y"))
        date = input().strip()
        if len(date) == 10:
            full_date = fulldate(date)
            if month <= 12:
                break
        print('INVALID! Date must be in format MM/DD/YYYY')

    while True:
        print(c["RED"] + 'ZULU TIME(HR:MN): ' + c["RESET"], end='')
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
        print(c["RED"] + 'STATION: ' + c["RESET"], end='')
        time.sleep(0.1)
        # kb.SendKeys('YUL', pause=0)
        pyautogui.write('YUL')
        station = input().strip().upper()
        if station.isalpha() and len(station) == 3:
            break
        print('INVALID! Station must contain only 3 letters')

    while True:
        print(c["RED"] + 'RESOLUTION: ' + c["RESET"], end='')
        time.sleep(0.1)
        # kb.SendKeys('INSP/CHK', pause=0)
        pyautogui.write('INSP/CHK')
        resolution = input().strip().upper()
        if len(resolution) > 0:
            break
        print('INVALID!')

    while True:
        print(c["RED"] + 'LOGPAGE: ' + c["RESET"], end='')
        logpage = input().strip()
        if logpage:
            first = logpage[0]
            if logpage.isdecimal() or first == 'f' or first == 'F':
                break
        print('INVALID logpage format')

    trax_dict = {'MECHANIC': name, 'DATE': full_date, 'HR:MN': hr + ':' + mn,
                 'RESOLUTION': resolution, 'STATION': station, 'LOGPAGE': logpage}


def fulldate(d):
    global month
    months_dict = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL',
                   8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}
    month = int(d[0] + d[1])
    day = int(d[3] + d[4])
    year = int(d[6] + d[7] + d[8] + d[9])

    return str(day) + ' ' + months_dict.get(month) + ' ' + str(year)
