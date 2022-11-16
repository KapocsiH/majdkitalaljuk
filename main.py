from menu import menu
from functions import newPerson, modifyPerson, whichPerson, deletePerson, readFile, detailsPerson, registration, matchmaker
from menu import menu2, menu3

readFile()

choice=menu()
while choice!=0:
    if choice==1:
        menu2()
    elif choice==2:
        menu3()
choice=menu()

