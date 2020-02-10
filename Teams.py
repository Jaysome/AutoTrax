import csv
import random
import time
import sys

acaCsv = open('aca.csv')
reader = csv.reader(acaCsv)
teamsList = list(reader)
onlyAca = []
for singleList in teamsList:
    onlyAca = onlyAca + singleList[2:]


def validate(user):
    if user in onlyAca:
        for team in teamsList:
            if user in team:
                teamname = team[0]
                luck = int(team[1])
                print('You are ' + adjectivate(luck) + ' member of ' + teamname + '.')
                break
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
         'an invaluable', 'an outstanding', 'a spectacular', 'an astonishing', 'a dazzling',
         'a bright', 'a ravishing', 'a captivating', 'an attractive', 'a charming', 'a delightful',
         'an irresistible', 'a graceful', 'an ineffable', 'a unique', 'a peerless',
         'an unparallelled', 'a champion'])
    medium_adjectives = random.choice(
        ['a', 'a', 'a', 'a capable', 'a common', 'a confirmed', 'a conventional', 'a decent',
         'a fair', 'a fair enough', 'a good enough', 'a humble', 'a known', 'a legitimate',
         'a moderate', 'a normal', 'a not bad', 'a not too bad', 'a passable', 'a permitted',
         'a presentable', 'a proper', 'a recognized', 'a regular', 'a sanctioned', 'a satisfactory',
         'a standard', 'a sufficient', 'a suitable', 'a typical', 'a valid',
         'a validated', 'an acceptable', 'an accepted', 'an acknowledged', 'an adequate',
         'an admissible', 'an all right', 'an allowable', 'an allowed', 'an approved',
         'an authorized', 'an average', 'an identified', 'a classic'])

    roll = random.randint(0, 100)

    if roll <= luck:
        return good_adjectives
    else:
        return medium_adjectives
