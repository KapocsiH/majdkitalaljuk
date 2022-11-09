import os

def menu():
    print('1...Kamu profil létrehozása')
    print('2...Kamu profil módosítása')
    print('3...Keresés a kamu profilok között(szűréssel)')
    print('4...Nem kívánatos kamu profil eltávolítása')
    print('5...Matchmaker --> Leíráshoz nyomja meg a 6-os gombot!')
    print('0...Kilépés az admin felületről')

    choice=input('\nVálasztás (0..6)')
    while len(choice)!=1 or choice<'0' or choice>'6':
        choice=input('\nVálasztás (0..6)')

    