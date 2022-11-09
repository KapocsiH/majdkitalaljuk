from data import *

people = []

def readFile():
    f = open('Munkafüzet1.csv', 'r', encoding='UTF-8')
    f.readline() # bevezető sor átlépése
    for row in f:
        r = Rednit(row.strip())
        people.append(r)
    f.close()

    return people