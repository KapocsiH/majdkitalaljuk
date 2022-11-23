import os
from functions import *

def menu():
    print('1...Admin felület')
    print('2...Normál felhasználói felület')
    print('3...Kilépés a programból')
 

    choice=input('\nVálasztás (1..3): ')
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
    
    choice=input('\nVálasztás (1..4): ')

    if choice=='1':
        whichPerson()
    elif choice=='2':
        newPerson()
    elif choice=='3':
        modifyPerson()
    elif choice=='4':
        deletePerson()
    elif choice=='5':
        return 


def menu3():     
    print('1...Emberek keresése')
    print('2...Regisztráció')
    print('3...Matchmaker')
    print('4...Vissza')

    choice=input('\nVálasztás (1..4): ')

    if choice=='1':
        detailsPerson()
    elif choice=='2':
        pass
    elif choice=='3':
        matchmaker()
    elif choice=='4':
        return
    
def registration():
    password = 'Adminuser'
    login = input('Kérem a jelszót:  ')
    if login == password:
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
                print('\nSikertelen bejelnetkezés, innentől a normál felületben folytathatja az alkalmazás használatát!\n')
                menu3()