from clear import clear
from models.user import *
import database

def login():
    wrong_login = False
    while (True):
        clear()

        
        if(wrong_login):
            print("Wrong login. Try again.")
            wrong_login = False

        user=input("Enter username: ")
        password=input("Enter password: (pssst its 123)  ")

        if user.upper()=="CSO" and password=="123":
            database.currentUser.id = 0
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'CSO'

        elif user.upper()=="SCSO" and password=="123":
            database.currentUser.id = 1
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'SCSO'

        elif user.upper()=="AM" and password=="123":
            database.currentUser.id = 2
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'AM'

        elif user.upper()=="FM" and password=="123":
            database.currentUser.id = 3
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'FM'

        elif user.upper()=="SM" and password=="123":
            database.currentUser.id = 4
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'SM'

        elif user.upper()=="PM" and password=="123":
            database.currentUser.id = 5
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'PM'
        
        elif user.upper()=="HRTM" and password=="123":
            database.currentUser.id = 6
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'HRTM'

        elif user.upper()=="STM" and password=="123":
            database.currentUser.id = 7
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'STM'
        
        else:
            wrong_login = True
            continue
        break
    return

