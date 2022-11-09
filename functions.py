from data import Rednit

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
    f = open('Munkafüzet.csv', 'w', encoding='UTF-8')
    for r in people:
        row = f'{r.name};{r.module};{r.time};{r.percent}\n'
        f.write(row)
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

def newPerson():
    name = input('Név: ')
    age = int(input('Kor: '))
    gender = input('Nem: ')
    residence = input('Lakhely: ')
    children = int(input('Utódok száma: '))
    sexuality = input('Vonzalom: ')
    row = f'{name};{age};{gender};{residence};{children};{sexuality}\n'
    f = open('Munkafüzet1.csv', 'a', encoding = 'UTF-8')
    f.write(row)
    f.close
    r = Rednit(row)
    people.append(r)

def modifyPerson():
    name = input('Név: ')
    for p in people:
        if p.name.lower() == name.lower():
            p.age = int(input('Kor: '))
            p.gender = input('Nem: ')
            p.residence = input('Százalék: ')
            p.children = int(input('Utódok száma: '))
            p.sexuality = input('Vonzalom: ')
            writeFile()
            return
    input('Ilyen nevű felhasználó nincs.')

def detailsPerson():
    name = input('Név(részlet):  ')
    for r in people:
        if name.lower() in r.name.lower():
            print(f'{r.name}, {r.age} éves {r.gender}. Lakhelye {r.residence}, {r.children} utódja van. Szexualitása {r.sexuality}. ')
    
    input('')



def deletePerson():
    name = input('Név: ')
    for i in people:
        if r.name.lower() in name.lower():
            people.remove(i)
            writeFile()
            return
    r = Rednit(row)
    people.pop(r)
    input('Ilyen nevű profil nincsen')
