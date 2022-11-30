import os
import sys
from functions import *
from colorama import init
from termcolor import colored

def menu():
    init()
    print(colored('1...Admin felület              ','white', 'on_magenta'))
    print(colored('2...Normál felhasználói felület','white', 'on_yellow'))
    print(colored('3...Kilépés a programból       ','white', 'on_cyan'))
 
    choice=input(colored('\nVálasztás (1..3): ','cyan', 'on_grey'))
    while len(choice)!=1 or choice<'1' or choice>'3':
        choice=input('\nVálasztás (0..3): ')

    os.system('cls')
    return int(choice)

def menu2():
    init()
    print(colored('1...Emberek keresése     ', 'white', 'on_red'))
    print(colored('2...Új profil létrehozása', 'white','on_yellow'))
    print(colored('3...Adatok módosítása    ', 'white', 'on_yellow'))
    print(colored('4...Profilok törlése     ', 'white', 'on_green'))
    print(colored('5...Vissza               ', 'white', 'on_blue'))
    print(colored('6...Kilépés a programból ', 'white', 'on_magenta'))
    
    choice=input(colored('\nVálasztás (1..6): ','cyan'))

    while choice!=7:
        if choice=='1':
            detailsPerson()
            os.system('cls')
            return
        elif choice=='2':
            newPerson()
            os.system('cls')
            return
        elif choice=='3':
            modifyPerson()
            os.system('cls')
            return
        elif choice=='4':
            deletePerson()
            os.system('cls')
            return
        elif choice=='5':
            os.system('cls')
            return
        elif choice=='6':
            sys.exit()

def menu3():     
    print(colored('1...Emberek keresése    ','white', 'on_magenta'))
    print(colored('2...Regisztráció        ','grey', 'on_white'))
    print(colored('3...Matchmaker          ','white', 'on_magenta'))
    print(colored('4...Vissza              ','white','on_grey'))
    print(colored('5...Kilépés a programból','white','on_blue'))

    choice=input(colored('\nVálasztás (1..5): ','cyan'))

    while choice!=6:
        if choice=='1':
            detailsPerson()
            os.system('cls')
            return
        elif choice=='2':
            newPerson()
            os.system('cls')
            return
        elif choice=='3':
            matchmaker()
            os.system('cls')
            return
        elif choice=='4':
            os.system('cls')
            return
        elif choice=='5':
            sys.exit()

def menuRestricted():
    print('1...Emberek keresése')
    print('2...Kilépés a programból')

    choice=input(colored('\nVálasztás (1..2): ','cyan'))

    while choice!=3:
        if choice=='1':
            detailsPerson()
            os.system('cls')
            menuRestricted()
        elif choice=='2':
            sys.exit()
    
def registration():
    password = 'Adminuser'
    login = input(colored('Kérem a jelszót:  ','cyan'))
    if login == password:
        os.system('cls')
        menu2()
    elif login != password:
        login = input(colored('Kérem a jelszót:  ','cyan'))
        if login == password:
            menu2()
        elif login != password:
            login = input(colored('Kérem a jelszót:  ','cyan'))
            if login == password:
                menu2()
            else:
                input('\nSikertelen bejelentkezés, innentől a korlátolt felületben folytathatja az alkalmazás használatát.\n\nEnterrel továbbléphet a menübe.')
                os.system('cls')
                menuRestricted()