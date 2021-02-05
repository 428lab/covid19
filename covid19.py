# -*- coding: utf-8 -*-
import random

def stayAtHome(you):
    you["stay_at_home"] = True

def washHands(you):
    you["wash_hands"] = True

def maintainSocialDistancing(you):
    you["sodial_distancing"] = True

def stilCovid19(everyone):
    for you in everyone:
        if(you["stay_at_home"] == False):
            return True
        if(you["wash_hands"] == False):
            return True
        if(you["sodial_distancing"] == False):
            return True
    return False

def takeOffTheMask(everyone):
    print('じんるいは　マスクを　はずした')

def letsGoOutForSomeDrinks(everyone):
    print('じんるいは　そとに　でられるようになった')

print('ｼｮｷｶﾁｭｳ・・・')
human = {"stay_at_home": False,"wash_hands": False,"sodial_distancing": False}
everyone = []
for i in range(126500000):
    everyone.append(human)

covid19 = True

print('しんがたコロナウイルスが　あらわれた')
while(covid19):

    print('じんるいは　いえから　でないように　した')
    print('じんるいは　てを　あらった')
    print('じんるいは　てきせつな　きょりをとって　よけた')
    
    print('ｾﾝﾄｳﾁｭｳ・・・')
    for you in everyone:
        stayAtHome(you)
        washHands(you)
        maintainSocialDistancing(you)

    covid19 = stilCovid19(everyone)

print('しんがたコロナウイルスを　たおした')

takeOffTheMask(everyone)
letsGoOutForSomeDrinks(everyone)

