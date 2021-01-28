#программа должна делать карточку пользователя с помощью рандома
#1. генерирует номер карточки и начальные показатели
#2. дальше делаем систему транзакций, изменяя параметры объекта(карты)
#3. просмотр карты, а так же перевод из одной валюты, в другую

#система
#будет объект банковская карта с параматерами по умолчанию, а именно номер карты, сколько там денег
#будут так же карты привязанные к родительским картам, типо как junior. Там будет лимит в переводе средств

#26.12
#сделать перевод валюты с помощью деления суммы, а так же сделать валюту как переменная в объекте
#сделать возможность добавления нескольких карт, с помощью сохранения файла card, card2, card3, и будет проверяться наличие файла, если он есть, то создается следующий. Будет лимит карт
#сделать наследование junior карту

#27.12
#доделать перевод валют, там требуется дописать перевод с какой-то валюты в какую-то, и наоборот, нужно просто время и терпение

#30.12
#надо к каждому блоку в выбором, добавить текст, по типу "чтобы выйти, напишите - exit", или какая-то заметка
#а так же заменить данными заметками или подсказкой, фунцию help, и вырезать ее. И там где она выхывается, заменить подсказками, или ещё чем
#сделать систему кредитов с процентами, которые привязанные с временем, а так же меню где будет отслеживаться, сколько надо выплатить и сроки

#не забыть про добавлению функции нескольких карт, а еще лучше сделать их неограниченное количество, с помощью for и проверки card1, card2, card3...
#потом надо будет окрыть все card-образные файлы и вглянуть на их информацию, все уместить в for, так как у кажого сохранения будет свой порядковый номер

#31.12
#ещё не сделана функция нескольких карт и кредитов
#с новым годом! надеюсь 2021 будет ещё лучше! :)

#03.01
#доделать кредиты

#04.01
#доделать систему нескольких карт, и сделать все по-красивому
#требуется функция выбора какой-то из карты, и удаления, или замена какой-то карты

#05.01
#сделать систему кредитов адекватной
#сделать интерфейс красивее и красочней
#сделать систему удаления и замены карт

#07.01
#сделать более красивый интерфейс
#нормальные кредиты
#скомпилировать и поверить работу всей программу

#07.01 17:00
#Баг: из карты можно вывести больше чем есть
#при замене карты, программма вылетает (но по какой-то причине, карта 0 заменяется)

#09.01
#кастомизировать программу, и везде добавить функцию exit
#скомпилировать и сделать дебаггинг


#17.01
#сделать перевод валюты долга, при смене валюты счета

#23.01.2021
#работа над програмой завершена

import random
from colorama import Fore, Back, Style
import sys
import os
import pickle
import math
from functions import *

class Card:
    def __init__(self, number, money, password, valuta, debt):
        self.number = number
        self.money = money
        self.password = password
        self.valuta = valuta
        self.debt = debt

    def short_info(self):
        return self.number

    def info(self):
        return (self.number, self.money, self.valuta, self.debt)

    def login_card(self):
        while True:
            try_log = input('Введите пароль: ')
            if try_log != self.password:
                print('Неправильно!')
            elif try_log == self.password:
                print('Введён верный пароль')
                break

    def get_pass(self):
        return self.password

    def get_val(self):
        return self.valuta

    def get_info(self):
        return(self.number, self.money, self.password, self.valuta, self.debt)

    def check_cred(self):
        return self.debt

def new_card(number_of_savefile):
    num1 = random.randint(1000, 9999)
    num2 = random.randint(1000, 9999)
    num3 =  random.randint(1000, 9999)
    number = '7568 {0} {1} {2}'.format(num1, num2, num3)
    money = 0
    debt = 0
    while True:
        password = input('Введите пароль для карты: ')
        valuta = 'грн'        
        if password == '':
            print('Ваш пароль должен содержать минимум 1 символ\nДля прервания операции, введите exit')
            continue
        elif password == 'exit':
            break
        else:
            cards = Card(number, money, password, valuta, debt)
            name_file = 'cards{0}'.format(number_of_savefile)
            s = open(name_file, 'wb')
            pickle.dump(cards, s)
            s.close()
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

cards0 = ''
cards1 = ''
cards2 = ''
cards3 = ''
cards4 = ''

if os.path.exists('cards0') == True:
    e = open('cards0', 'rb')
    cards0 = pickle.load(e)
else:
    pass

if os.path.exists('cards1') == True:
    r = open('cards1', 'rb')
    cards1 = pickle.load(r)
else:
    pass

if os.path.exists('cards2') == True:
    t = open('cards2', 'rb')
    cards2 = pickle.load(t)
else:
    pass

if os.path.exists('cards3') == True:
    y = open('cards3', 'rb')
    cards3 = pickle.load(y)
else:
    pass

if os.path.exists('cards4') == True:
    u = open('cards4', 'rb')
    cards4 =pickle.load(u)
else:
    pass

present_list = []

numb = ''
mone = ''
passwo = ''
val = ''
debt = ''

while True:
    while True:
        clear()
        print(Back.GREEN + 'Вас привествует ЖопаБанк')
        print(Back.RED + 'Обязательно введите help, если запускается программу впервые!')
        print(Style.RESET_ALL)

        if os.path.exists('cards0') or os.path.exists('cards1') or os.path.exists('cards2') or os.path.exists('cards3') or os.path.exists('cards4') == False:
            print(Fore.BLUE + 'Для создания новой карты, введите new{0}'.format(Style.RESET_ALL))
            print('')

        for i in range(0, 5):
            name_filecard = 'cards{0}'.format(i) 
            if os.path.exists(name_filecard) == True:
                f = open(name_filecard, 'rb')
                cards = pickle.load(f)
                print('{0}. Номер карты {1}\n'.format(i, cards.short_info()))
            else:
                pass
                    
        card0 = False
        card1 = False
        card2 = False
        card3 = False
        card4 = False

        passw = ''
        true_pass = ''

        if os.path.exists('cards') != False:
            true_pass = cards.get_pass()

        w = input('Введите команду: ')
        if w == 'new':
            clear()
            if os.path.exists('cards0') and os.path.exists('cards1') and os.path.exists('cards2') and os.path.exists('cards3') and os.path.exists('cards4') == True:
                while True:
                    clear()
                    for i in range(0, 5):
                        name_filecard = 'cards{0}'.format(i) 
                        if os.path.exists(name_filecard) == True:
                            f = open(name_filecard, 'rb')
                            cards = pickle.load(f)
                            print('{0}. Номер карты {1}\n'.format(i, cards.short_info()))
                        else:
                            pass
                    print('Лимит карт достигнут, введите номер карты, чтобы её удалить')
                    print('Или введите exit для выхода')
                    choose_replace = input('')
                    if choose_replace == '0':
                        e.close()
                        f.close()
                        os.remove('cards0')
                        new_card(0)
                        break
                    elif choose_replace == '1':
                        r.close()
                        f.close()
                        os.remove('cards1')
                        new_card(1)
                        break
                    elif choose_replace == '2':
                        t.close()
                        f.close()
                        os.remove('cards2')
                        new_card(2)
                        break
                    elif choose_replace == '3':
                        y.close()
                        f.close()
                        os.remove('cards3')
                        new_card(3)
                        break
                    elif choose_replace == '4':
                        u.close()
                        f.close()
                        os.remove('cards4')
                        new_card(4)
                        break

            else:
                num1 = random.randint(1000, 9999)
                num2 = random.randint(1000, 9999)
                num3 =  random.randint(1000, 9999)
                number = '7568 {0} {1} {2}'.format(num1, num2, num3)
                money = 0
                debt = 0
                while True:
                    password = input('Введите пароль для карты: ')
                    valuta = 'грн'        
                    if password == '':
                        print('Ваш пароль должен содержать минимум 1 символ\nДля прервания операции, введите exit')
                        continue
                    elif password == 'exit':
                        break
                    else:
                        cards = Card(number, money, password, valuta, debt)
                        num_file = check_cards()
                        name_file = 'cards{0}'.format(num_file)
                        s = open(name_file, 'wb')
                        pickle.dump(cards, s)
                        s.close()
                        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)



        elif w == 'help':
            print('Для создания новой карты, введите - new')
            print('Для входа в карту, введите - login')
            print('Для удаления карты, введите - del')

        elif w == 'login':
            clear()
            for i in range(0, 5):
                name_filecard = 'cards{0}'.format(i) 
                if os.path.exists(name_filecard) == True:
                    f = open(name_filecard, 'rb')
                    cards = pickle.load(f)
                    print('{0}. Номер карты {1}\n'.format(i, cards.short_info()))
                else:
                    pass
            while True:
                number_of_card = input('Введите номер карты в которую хотите войти\n')
                if number_of_card == '0':
                    if os.path.exists('cards0') == True:
                        true_pass = cards0.get_pass()
                        card0 = True
                        break
                    else:
                        print('Вы ввели номер несуществующей карты')
                        continue

                elif number_of_card == '1':
                    if os.path.exists('cards1') == True:
                        true_pass = cards1.get_pass()
                        card1 = True
                        break
                    else:
                        print('Вы ввели номер несуществующей карты')
                        continue

                elif number_of_card == '2':
                    if os.path.exists('cards2') == True:
                        true_pass = cards2.get_pass()
                        card2 = True
                        break
                    else:
                        print('Вы ввели номер несуществующей карты')
                        continue  

                elif number_of_card == '3':
                    if os.path.exists('cards3') == True:
                        true_pass = cards3.get_pass()
                        card3 = True
                        break
                    else:
                        print('Вы ввели номер несуществующей карты')
                        continue  

                elif number_of_card == '4':
                    if os.path.exists('cards4') == True:
                        true_pass = cards4.get_pass()
                        card4 = True
                        break
                    else:
                        print('Вы ввели номер несуществующей карты')
                        continue 

                elif number_of_card == 'exit':
                    break

                else:
                    print('Введите exit для отмены операции') 
                
            failure_login = True
            failure_login = log(passw, true_pass, failure_login) # True - вход провалился, False - вход успешен
            if failure_login == True:
                session = False
                break
            else:
                print('Вы успешно вошли в карту')
                session = True
                break

        elif w == 'del':
            clear()
            for i in range(0, 5):
                name_filecard = 'cards{0}'.format(i) 
                if os.path.exists(name_filecard) == True:
                    f = open(name_filecard, 'rb')
                    cards = pickle.load(f)
                    print('{0}. Номер карты {1}\n'.format(i, cards.short_info()))
                else:
                    pass

            while True:
                del_card = input('Введите номер карты, которую вы хотите удалить\n')
                if del_card == '0':
                    if os.path.exists('cards0') == True:
                        e.close()
                        f.close()
                        os.remove('cards0')
                        break
                    else:
                        print('Такой карты не существует')
                        continue
                    
                elif del_card == '1':
                    if os.path.exists('cards1') == True:
                        r.close()
                        f.close()
                        os.remove('cards1')
                        break
                    else:
                        print('Такой карты не существует')
                        continue

                elif del_card == '2':
                    if os.path.exists('cards2') == True:
                        t.close()
                        f.close()
                        os.remove('cards2')
                        break
                    else:
                        print('Такой карты не существует')
                        continue

                elif del_card == '3':
                    if os.path.exists('cards3') == True:
                        y.close()
                        f.close()
                        os.remove('cards3')
                        break
                    else:
                        print('Такой карты не существует')
                        continue

                elif del_card == '4':
                    if os.path.exists('cards4') == True:
                        u.close()
                        f.close()
                        os.remove('cards4')
                        break
                    else:
                        print('Такой карты не существует')
                        continue

                elif del_card == 'exit':
                    break

        else:
            print('Введите help для помощи, или exit для выхода из карты')

    if card0 == True:
        cards = cards0
    if card1 == True:
        cards = cards1
    if card2 == True:
        cards = cards2
    if card3 == True:
        cards = cards3
    if card4 == True:
        cards = cards4

    while session == True:
        if session == False:
            break
        while True:
            save_open = save_card(card0, card1, card2, card3, card4)
            clear()
            present(cards, present_list)
            print(Fore.GREEN + '\nДля выхода из карты, введите - exit\n')
            print(Style.RESET_ALL)
            print('1 - провести транзакцию')
            print('2 - изменить валюту')
            print('3 - оформить кредит')
            check_debt = cards.check_cred()
            if_debt = False
            if check_debt > 0:
                print('4 - погасить кредит')
                if_debt = True

            com_card = input('')    
            if com_card == '1':
                clear()
                present(cards, present_list)
                print('')
                print('1 - пополнить карту')
                print('2 - вывести с нее средства')
                trans = input('')
                if trans == '1':
                    clear()
                    present(cards, present_list)
                    print('')
                    while True:
                        print('На сколько вы хотите пополнить карту?')
                        add_money = input('')
                        if int(add_money) < 0:
                            print('Введите плюсовое число')
                            print('Введите help для помощи, или exit для выхода из операции')
                            continue
                        else:
                            break
                    clear()
                    numb, mone, passwo, val, debt = cards.get_info()
                    add_mon = int(add_money) + mone
                    cardsss = Card(numb, add_mon, passwo, val, debt)
                    o = open(save_open, 'wb')
                    pickle.dump(cardsss, o)
                    o.close()
                    e = open(save_open, 'rb')
                    cards = pickle.load(e)
                    present(cards, present_list)
                    break

                if trans == '2':
                    clear()
                    present(cards, present_list)
                    print('')
                    while True:
                        print('Сколько вы хотите вывести денег?')
                        subtract_money = input('')
                        if int(subtract_money) > mone:
                            print('На счету нет денег')
                            print('Введите help для помощи, или exit для выхода из операции')
                            continue
                        else:
                            break
                    numb, mone, passwo, val, debt = cards.get_info()
                    sub_mon =  mone - int(subtract_money)
                    cardsss = Card(numb, sub_mon, passwo, val, debt)
                    o = open(save_open, 'wb')
                    pickle.dump(cardsss, o)
                    o.close()
                    e = open(save_open, 'rb')
                    cards = pickle.load(e)
                    present(cards, present_list)
                    break
                if trans == 'exit':
                    break
                else:
                    print('Введите корректный номер, или exit для завершения операции')

            if com_card == '2':
                clear()
                present(cards, present_list)
                print('')
                while True:
                    print('Выберете валюту')
                    print('')
                    print('1 - грн')
                    print('2 - руб')
                    print('3 - доллары')
                    print('4 - евро')
                    numb, mone, passwo, val, debt = cards.get_info()
                    val_val = input('')
                    if val_val == '1': #гривни
                        if val == 'грн': #гривни в гривни
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'руб':
                            mone = transition(mone, 'rub', 'uah')
                            debt = transition(debt, 'rub', 'uah')
                            val = 'грн'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'евр':
                            mone = transition(mone, 'eur', 'uah')
                            debt = transition(debt, 'eur', 'uah')
                            val = 'грн'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'долл':
                            mone = transition(mone, 'dollar', 'uah')
                            debt = transition(debt, 'dollar', 'uah')
                            val = 'грн'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break

                    if val_val == '2': #рубли
                        if val == 'грн':
                            mone = transition(mone, 'uah', 'rub')
                            debt = transition(debt, 'uah', 'rub')
                            val = 'руб'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'руб':
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'долл':
                            mone = transition(mone, 'dollar', 'rub')
                            debt = transition(debt, 'dollar', 'rub')
                            val = 'руб'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'евро':
                            mone = transition(mone, 'euro', 'rub')
                            debt = transition(debt, 'euro', 'rub')
                            val = 'руб'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break 

                    if val_val == '3': #доллары
                        if val == 'грн':
                            mone = transition(mone, 'uah', 'dollar')
                            debt = transition(debt, 'uah', 'dollar')
                            val = 'долл'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'руб':
                            mone = transition(mone, 'rub', 'dollar')
                            debt = transition(debt, 'rub', 'dollar')
                            val = 'долл'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'долл':
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'евро':
                            mone = transition(mone, 'euro', 'dollar')
                            debt = transition(debt, 'euro', 'dollar')
                            val = 'долл'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                    if val_val == '4':
                        if val == 'грн':
                            mone = transition(mone, 'uah', 'euro')
                            debt = transition(debt, 'uah', 'euro')
                            val = 'евро'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'руб':
                            mone = transition(mone, 'rub', 'euro')
                            debt = transition(debt, 'rub', 'euro')
                            val = 'евро'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                        elif val == 'долл':
                            mone = transition(mone, 'dollar', 'euro')
                            debt = transition(debt, 'dollar', 'euro')
                            val = 'евро'
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break                                 
                        elif val == 'евро':
                            cardsss = Card(numb, mone, passwo, val, debt)
                            o = open(save_open, 'wb')
                            pickle.dump(cardsss, o)
                            o.close()
                            e = open(save_open, 'rb')
                            cards = pickle.load(e)
                            present(cards, present_list)
                            break
                    if val_val == 'exit':
                        break 
                    else:
                        print('Введите корректный номер, или exit для завершения задачи')

            if com_card == '3':
                clear()
                valutaaa = cards.get_val()
                present(cards, present_list)
                print('')
                uah = False
                rub = False
                dollar = False
                eur = False
                while True:
                    if valutaaa == 'грн':
                        uah = True
                        print('На сколько вы хотите взять кредит? Максимум - 10.000 грн.')
                    elif valutaaa == 'руб':
                        rub = True
                        print('На сколько вы хотите взять кредит? Максимум - 20.000 руб.')
                    elif valutaaa == 'долл':
                        dollar = True
                        print('На сколько вы хотите взять кредит? Максимум - 5.000 долл.')
                    if valutaaa == 'евро':
                        eur = True
                        print('На сколько вы хотите взять кредит? Максимум - 5.000 евро.')
                
                    money_get = input('')
                    if uah == True:
                        if int(money_get) >= 10000:
                            print('Введите сумму не выше 10.000')
                            continue
                        else:
                            break

                    elif rub == True:
                        if int(money_get) >= 20000:
                            print('Введите сумму не выше 20.000')
                            continue
                        else:
                            break

                    elif dollar == True:
                        if int(money_get) >= 5000:
                            print('Введите сумму не выше 5.000')
                            continue
                        else:
                            break

                    elif uah == True:
                        if int(money_get) >= 5000:
                            print('Введите сумму не выше 5.000')
                            continue
                        else:
                            break
                    else:
                        print('Введите корректную сумму')
                        continue

                numbeer = ''
                moneey = ''
                passwoord = ''
                valutaaa = ''
                deebt = ''
                numbeer, moneey, passwoord, valutaaa, deebt = cards.get_info()
                #[0self.number, 1self.money, 2self.password, 3self.valuta, 4self.debt]
                money_debt = math.ceil(int(money_get) * 1.5)
                deebt = int(money_debt)
                moneey = int(moneey) + int(money_get)
                cardsss = Card(numbeer, moneey, passwoord, valutaaa, math.ceil(deebt))
                o = open(save_open, 'wb')
                pickle.dump(cardsss, o)
                o.close()
                e = open(save_open, 'rb')
                cards = pickle.load(e)
                present(cards, present_list)

            if com_card == '4':
                clear()
                present(cards, present_list)
                if if_debt == False:
                    print('Введите корректный номер, или exit для завершения операции')
                else:
                    numb = ''
                    mon = ''
                    passwo = ''
                    valu = ''
                    debb = ''
                    numb, mon, passwo, valu, debb = cards.get_info()
                    if mon < debb:
                        print('У вас недостаточно средств для погашения кредита')
                        f = input('')
                    else:
                        balance = mon - debb
                        print('Если вы погасите кредит, на вашем счету останется {0} {1}.'.format(balance, valu))
                        print('Вы уверены в том чтобы погасить кредит?(y,n)')
                        decision = input('')
                        while True:
                            if decision == 'y' or 'Y':
                                debb = 0
                                print(numb, balance, passwo, valu, debb)
                                cardss = Card(numb, balance, passwo, valu, debb)
                                x = open(save_open, 'wb')
                                pickle.dump(cardss, x)
                                x.close()
                                c = open(save_open, 'rb')
                                cards = pickle.load(c)
                                break   
                            
                            if decision == 'n' or 'N':
                                l = input('')
                                break
                           
                            else:
                                print('Введите корректное значение')
                                continue

            elif com_card == 'exit':
                session = False
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                break

            else:
                print('Введите корректный номер, или exit для завершения операции')