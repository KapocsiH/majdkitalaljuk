from functions import people
from dataLaci import Rednit
r=Rednit()

def deletePerson():
    name=input('Név: ')
    for i in people:
        if r.name.lower() in name.lower():
            people.remove(i)
            writeFile()
            return
    input('Ilyen nevű profil nincsen')
