from dataLaci import *

people = []

def readFile():
    f = open('Munkafüzet1.csv', 'r', encoding='UTF-8')
    f.readline()
    for row in f:
        r = Rednit(row.strip())
        people.append(r)
    f.close()

    return people

def writeFile():
    f = open('people.csv', 'w', encoding='UTF-8')
    for person in people:
        f.write(f'{person}\n')
    f.close()
    

def whichPerson():
        name = input('Keresés: ')
        indexes = []
        for i in range(0, len(people)):
            if name.lower() in people[i].lower():
                indexes.append(i)

        number = 1
        for index in indexes:
            print(f'{number}..{people[index]}')
            menu += 1
        print('0..Vissza')

        choice = input('\nVálasztás: ')
        while not choice.isnumeric() or int(choice) < 0 or int(choice) > len(indexes):
            choice = input('\nHibás parancs, válasszon újra: ')

        if choice == 0:
            return -1
        else:
            return indexes[int(choice) - 1]

def modifyPerson():
    index = whichPerson()
    print('Módosítható adatok: név, kor, utód és lakhely')
    menu = input('Mit szeretne módosítani?')
    if menu.lower() == 'név':
        name(people[index]) = input('Módosított név:  ')
    elif menu.lower() == 'kor':
        age(people[index])