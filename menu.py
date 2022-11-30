import os
import sys
from functions import *
from colorama import init
from termcolor import colored

def menu():
    init()
    print(colored('1...Admin felület' ,'magenta', 'on_white'))
    print(colored('2...Normál felhasználói felület','white', 'on_magenta'))
    print(colored('3...Kilépés a programból','magenta', 'on_white'))
 
    choice=input(colored('\nVálasztás (1..3): ','white', 'on_magenta'))
    while len(choice)!=1 or choice<'1' or choice>'3':
        choice=input('\nVálasztás (0..3): ')

    os.system('cls')
    return int(choice)

def menu2():
    print('1...Emberek keresése')
    print('2...Új profil létrehozása')
    print('3...Adatok módosítása')
    print('4...Profilok törlése')
    print('5...Vissza')
    print('6...Kilépés a programból')
    
    choice=input('\nVálasztás (1..6): ')

    while choice!=7:
        if choice=='1':
            detailsPerson()
            os.system('cls')
            menu2()
        elif choice=='2':
            newPerson()
            os.system('cls')
            menu2()
        elif choice=='3':
            modifyPerson()
            os.system('cls')
            menu2()
        elif choice=='4':
            deletePerson()
            os.system('cls')
            menu2()
        elif choice=='5':
            os.system('cls')
            menu() 
        elif choice=='6':
            sys.exit()

def menu3():     
    print('1...Emberek keresése')
    print('2...Regisztráció')
    print('3...Matchmaker')
    print('4...Vissza')
    print('5...Kilépés a programból')

    choice=input('\nVálasztás (1..5): ')

    while choice!=6:
        if choice=='1':
            detailsPerson()
            os.system('cls')
            menu3()
        elif choice=='2':
            newPerson()
            os.system('cls')
            menu3()
        elif choice=='3':
            matchmaker()
            os.system('cls')
            menu3()
        elif choice=='4':
            return
        elif choice=='5':
            sys.exit()

def menuRestricted():
    print('1...Emberek keresése')
    print('2...Kilépés a programból')

    choice=input('\nVálasztás (1..2): ')

    while choice!=3:
        if choice=='1':
            detailsPerson()
            os.system('cls')
            menuRestricted()
        elif choice=='2':
            sys.exit()
    
def registration():
    password = 'Adminuser'
    login = input('Kérem a jelszót:  ')
    if login == password:
        os.system('cls')
        menu2()
    elif login != password:
        login = input('Kérem a jelszót:  ')
        if login == password:
            menu2()
        elif login != password:
            login = input('Kérem a jelszót:  ')
            if login == password:
                menu2()
            else:
                input('\nSikertelen bejelentkezés, innentől a korlátolt felületben folytathatja az alkalmazás használatát.\n\nEnterrel továbbléphet a menübe.')
                os.system('cls')
                menuRestricted()