from menu import menu
from functions import newPerson, modifyPerson, deletePerson, readFile, detailsPerson, matchmaker
from menu import menu2, menu3, registration

readFile()
choice=menu()

while choice!=3:
    if choice== 1:
        registration()
    elif choice == 2:
        menu3()
    choice=menu()



