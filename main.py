from menu import menu
from functions import newPerson, modifyPerson, whichPerson, deletePerson, readFile, detailsPerson, registration, matchmaker
from menu import menu2, menu3

readFile()
choice=menu()

while choice!=0:
    if choice==1:
        if registration() == True:
            menu2()
            if choice==1:
                whichPerson()
            if choice==2:
                newPerson()
            if choice==3:
                modifyPerson()
            if choice==4:
                deletePerson()
        else:
            menu3()
            if choice==1:
                detailsPerson()
            if choice==2:
                registration()
            if choice==3:
                matchmaker()
    if choice==2:
        menu3()
    choice=menu()

