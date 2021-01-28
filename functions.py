import random
from colorama import Fore, Back, Style
import sys
import os
import pickle
import math

def clear():
    if sys.platform == 'win32' or 'cygwin':
        clear_com = 'cls'
    os.system(clear_com)

def save_card(card0, card1, card2, card3, card4):
    if card0 == True:
        return 'cards0'
    if card1 == True:
        return 'cards1'
    if card2 == True:
        return 'cards2'
    if card3 == True:
        return 'cards3'
    if card4 == True:
        return 'cards4'

def log(passw, true_pass, failure_login):
    loop = True
    while loop == True:
        passw = input('Введите пароль от карты: ')
        if passw == true_pass:
            loop = False
            failure_login = False
            return failure_login
        elif passw == 'exit':
            loop = False
            failure_login = True
            return failure_login
        elif passw != true_pass:
            print('Для завершения операции, введите exit')
            continue

def transition(summ, f_valute, s_valute):
    #оно должно узнавать валюту которая есть сейчас, и в которую надо перевести
    #валюту которая сейчас есть, перевод в гривни и из гривни делает в ту которую надо
    if f_valute == 'uah':
        if s_valute == 'rub':
            summ = summ * 3
        elif s_valute == 'uah':
            summ = summ
        elif s_valute == 'dollar':
            summ = summ / 28
        elif s_valute == 'euro':
            summ = summ / 34
    if f_valute == 'rub':
        if s_valute == 'rub':
            summ = summ
        elif s_valute == 'uah':
            summ = summ / 3
        elif s_valute == 'dollar':
            summ = summ / 74
        elif s_valute == 'euro':
            summ = summ / 90
    if f_valute == 'dollar':
        if s_valute == 'rub':
            summ = summ * 74
        elif s_valute == 'uah':
            summ = summ * 28
        elif s_valute == 'dollar':
            summ = summ
        elif s_valute == 'euro':
            summ = summ
    if f_valute == 'euro':
        if s_valute == 'rub':
            summ = summ * 90
        elif s_valute == 'uah':
            summ = summ * 34
        elif s_valute == 'dollar':
            summ = summ
        elif s_valute == 'euro':
            summ = summ
    return summ

def check_cards():
    for i in range(0, 5):
        path_file = 'cards{0}'.format(i)
        if os.path.exists(path_file) == False:
            return i

def present(cardz, present_list):
    present_list = cardz.info()
    print('Номер карты: '+ Fore.RED +'{0}{1}'.format(present_list[0], Style.RESET_ALL))
    print('Средств на карте: '+ Fore.YELLOW +'{0:.1f} {1}.{2}'.format(present_list[1], present_list[2], Style.RESET_ALL))
    if present_list[3] > 0:
        print('Долг: '+ Fore.BLUE +'{0:.1f} {1}.{2}'.format(present_list[3], present_list[2], Style.RESET_ALL))