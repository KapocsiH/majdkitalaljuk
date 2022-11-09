from menu import menu
from functions import *

readFile()

choice=menu()

while choice!=0:
    if choice==1:
        newPerson()
    if choice==2:
        modifyPerson()
    if choice==3:
        whichPerson()
    if choice==4:
        deletePerson()
    if choice==5:
        matchmaker()
    if choice==6:
        description()
    choice=menu()
    