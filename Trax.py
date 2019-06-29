import datetime
import random
import sys
import time

import pywinauto.keyboard as kb

import Teams

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
        print('\nMECHANIC: ', end='')
        name = input().strip().upper()
        if name.isalpha() and len(name) <= 8:
            break
        print('INVALID! Name must be exactly like in trax otherwise it fucks everything')

    validate(name)

    while True:
        print('CLOSED ON (MM/DD/YYYY): ', end='')
        now = datetime.datetime.utcnow()
        time.sleep(0.1)
        kb.SendKeys(now.strftime("%m/%d/%Y"), pause=0)
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
        kb.SendKeys('YUL', pause=0)
        station = input().strip().upper()
        if station.isalpha() and len(station) == 3:
            break
        print('INVALID! Station must contain only 3 letters')

    while True:
        print('RESOLUTION: ', end='')
        time.sleep(0.1)
        kb.SendKeys('INSP/CHK', pause=0)
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


def fulldate(d):
    global month
    months_dict = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL',
                   8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}
    month = int(d[0] + d[1])
    day = int(d[3] + d[4])
    year = int(d[6] + d[7] + d[8] + d[9])

    return str(day) + ' ' + months_dict.get(month) + ' ' + str(year)


def validate(user):
    if user in Teams.team_one:
        print('You are ' + adjectivate(100) + ' member of Team One.')
    elif user in Teams.team_snake:
        print('You are ' + adjectivate(20) + ' member of Team Snake.')
    elif user in Teams.team_calvin:
        print('You are an approved user.')
    else:
        print('You are not an approved user! Please contact your system administrator.')
        time.sleep(2)
        sys.exit()


def adjectivate(luck):
    good_adjectives = random.choice(
        ['a bold', 'a breathtaking', 'a brilliant', 'a celebrated', 'a charismatic', 'a cherished',
         'a chivalrous', 'a commendable', 'a competent', 'a dignified', 'a distinguished',
         'a dynamic', 'a fabulous', 'a fearless', 'a foremost', 'a gallant', 'a glorious',
         'a grandiose', 'a great', 'a legendary', 'a magnificient', 'a majestic', 'a marvelous',
         'a mighty', 'a model', 'a noble', 'a perfect', 'a phenomenal', 'a powerful', 'a precious',
         'a prized', 'a prodigious', 'a proud', 'a quality', 'a remarkable', 'a renowned',
         'a resplendent', 'a revered', 'a sexy', 'a solid', 'a splendid', 'a stalwart',
         'a striking', 'a stunning', 'a stupendous', 'a sublime', 'a super', 'a superb',
         'a superior', 'a treasured', 'a valiant', 'a valorous', 'a valuable', 'a venerated',
         'a wonderful', 'a worthy', 'an admirable', 'an amazing', 'an august', 'an elegant',
         'an eminent', 'an energetic', 'an esteemed', 'an exalted', 'an excellent',
         'an exceptional', 'an exemplary', 'an exquisite', 'an extraordinary', 'an heroic',
         'an honorable', 'an honored', 'an illustrious', 'an impeccable', 'an important',
         'an impressive', 'an inestimable', 'an influential', 'an intense', 'an intrepid',
         'an invaluable', 'an outstanding'])
    medium_adjectives = random.choice(
        ['a', 'a', 'a', 'a capable', 'a common', 'a confirmed', 'a conventional', 'a decent',
         'a fair', 'a fair enough', 'a good enough', 'a humble', 'a known', 'a legitimate',
         'a moderate', 'a normal', 'a not bad', 'a not too bad', 'a passable', 'a permitted',
         'a presentable', 'a proper', 'a recognized', 'a regular', 'a sanctioned', 'a satisfactory',
         'a standard', 'a sufficient', 'a suitable', 'a suitable', 'a typical', 'a valid',
         'a validated', 'an acceptable', 'an accepted', 'an acknowledged', 'an adequate',
         'an admissible', 'an all right', 'an allowable', 'an allowed', 'an approved',
         'an authorized', 'an average', 'an identified'])

    roll = random.randint(0, 100)

    if roll <= luck:
        return good_adjectives
    else:
        return medium_adjectives
