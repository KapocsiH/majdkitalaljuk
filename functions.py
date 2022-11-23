from data import Rednit
people = []
# choosenperson = []

def readFile():
    f = open('Munkafuzet.csv', 'r', encoding='UTF-8')
    f.readline()
    for row in f:
        r = Rednit(row.strip())
        people.append(r)
    f.close()

def writeFile():
    f = open('Munkafuzet.csv', 'w', encoding='UTF-8')
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
    writeFile()

def modifyPerson():
    choice = int(input('Mit akarunk változtatni?\n1= név\n2= kor\n3= nem\n4= lakhely\n5= utódok\n6= vonzalom:  '))
    for r in people:
        if whichPerson() == r.name.lower():
            pass

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

def registration():
    password = 'Adminuser'
    login = input('Kérem a jelszót:  ')
    if login == password:
        return True
    elif login != password:
        login = input('Kérem a jelszót:  ')
        if login == password:
            return True
        elif login != password:
            login = input('Kérem a jelszót:  ')
            if login == password:
                return True
            else:
                return False

def matchmaker():
    print('Mi alapján szeretne keresni?')
    print('1. Kor, 2. Nem, 3. Utódok száma, 4. Szexualitás')
    choice = int(input('Választás:  '))
    if choice == 1:
        print('Korkategória: ')
        print('1. -25')
        print('2. 26-45')
        print('3. 45-')
        agepreferance = input('Választás:  ')
        prefer = []
        if agepreferance == 1:
            for r in people:
                if r.age <= 25:
                    prefer.append(people[r])
        
        