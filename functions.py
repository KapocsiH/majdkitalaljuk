from data import Rednit
people = []
# choosenperson = []

def readFile():
    f = open('data.csv', 'r', encoding='UTF-8')
    f.readline()
    for row in f:
        r = Rednit(row.strip())
        people.append(r)
    f.close()

def writeFile():
    f = open('data.csv', 'w', encoding='UTF-8')
    for r in people:
        row = f'{r.name};{r.age};{r.gender};{r.residence};{r.children};{r.sexuality}\n'
        f.write(row)
    f.close()
    

def whichPerson():
    name = input('Kit keresünk? ')
    for r in people:
        if name.lower() in r.name.lower():
            choosenperson = r.name.lower()

    return choosenperson


def newPerson():
    name = input('Név: ')
    age = int(input('Kor: '))
    gender = input('Nem: ')
    residence = input('Lakhely: ')
    children = int(input('Utódok száma: '))
    sexuality = input('Vonzalom: ')
    row = f'{name};{age};{gender};{residence};{children};{sexuality}\n'
    f = open('data.csv', 'a', encoding = 'UTF-8')
    f.write(row)
    f.close
    r = Rednit(row)
    people.append(r)

def modifyPerson():
    name = input('A változtatni kívánt alany neve (teljes név): ')
    for r in people:
        if r.name.lower() == name.lower():
            r.gender = input('Nem: ')
            r.residence = input('Lakhely: ')
            r.children = int(input('Utódok száma: '))
            r.sexuality = input('Vonzalom: ')
            writeFile()
            return

def detailsPerson():
    name = input('Név:  ')
    for r in people:
        if name.lower() in r.name.lower():
            print(f'{r.name}, {r.age} éves {r.gender}. Lakhelye {r.residence}, {r.children} utódja van. Szexualitása {r.sexuality}. ')

    input('')



def deletePerson():
    name = input('Név: ')
    for r in people:
        if r.name.lower() == name.lower():
            people.remove(r)
            writeFile()
            return
    input('Ilyen nevű profil nincsen')


def matchmaker():
    print('Mi alapján szeretne keresni?')
    print('1. Kor, 2. Nem, 3. Utódok száma, 4. Szexualitás')
    choice = int(input('Választás:  '))
    while choice < 1 or choice > 4:
        choice = int(input('Választás:  '))
    if choice == 1:
        print('Korkategória:')
        print('1. -25')
        print('2. 26-45')
        print('3. 45-')
        agepreferance = input('Választás:  ')
        while agepreferance < 1 or agepreferance > 3:
            agepreferance = input('Választás:  ')
        suitable = []
        if agepreferance == 1:
            for r in people:
                if r.age <= 25:
                    suitable.append(people[r])
        elif agepreferance == 2:
            for r in people:
                if r.age >= 26 and r.age <= 45:
                    suitable.append(people[r])
        elif agepreferance == 2:
            for r in people:
                if r.age >= 26 and r.age <= 45:
                    suitable.append(people[r])
        print(f'Megfelelő profilok: {suitable}')
    elif choice == 2:
        print('Nemek:')
        print('1. Férfi')
        print('2. Nő')
        print('3. Egyéb')
        genderpreferance = int(input('Választás:  '))
        while genderpreferance < 1 or genderpreferance > 3:
            genderpreferance = int(input('Választás:  '))
        suitable = []
        if genderpreferance == 1:
            for r in people:
                if r.gender == 'férfi':
                    suitable.append(people[r])
        elif genderpreferance == 2:
            for r in people:
                if r.gender == 'nő':
                    suitable.append(people[r])
        elif genderpreferance == 3:
            print('Jelenleg nincs ilyen felhasználónk')
        print(f'Megfelelő profilok: {suitable}')
    elif choice == 3:
        print('Utódok száma:')
        print('1. Nincs utód')
        print('2. 1')
        print('3. 2')
        print('4. Több')
        childpreferance = int(input('Választás:  '))
        while childpreferance < 1 or childpreferance > 3:
            childpreferance = int(input('Választás:  '))
        suitable = []
        if childpreferance == 1:
            for r in people:
                if r.children == 0:
                    suitable.append(people[r])
        elif childpreferance == 2:
            for r in people:
                if r.children == 1:
                    suitable.append(people[r])
        elif childpreferance == 3:
            for r in people:
                if r.children == 2:
                    suitable.append(people[r])
        elif childpreferance == 4:
            for r in people:
                if r.children > 2:
                    suitable.append(people[r])
        print(f'Megfelelő profilok: {suitable}')
    elif choice == 4:
        print('Szexualitás:')
        print('1. Heteroszexuális')
        print('2. Homoszexuális')
        print('3. Egyéb')
        sexualitypreferance = int(input('Választás:  '))
        while sexualitypreferance < 1 or sexualitypreferance > 3:
            sexualitypreferance = int(input('Választás:  '))
        suitable = []
        if sexualitypreferance == 1:
            for r in people:
                if r.sexuality == 'Heteroszexuális':
                    suitable.append(people[r])
        elif sexualitypreferance == 2:
            for r in people:
                if r.sexuality == 'Homoszexuális':
                    suitable.append(people[r])
        elif sexualitypreferance == 3:
            for r in people:
                if r.sexuality == 'Egyéb':
                    suitable.append(people[r])
        print(f'Megfelelő profilok: {suitable}')