from clear import clear
from models.user import *
import database

def login():
    while True:
        clear()
        
        user=input("Enter username: ")
        password=input("Enter password: (pssst its 123)  ")

        if user=="CSO" and password=="123":
            database.currentUser.id = 0
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'CSO'
            return

        elif user=="SCSO" and password=="123":
            database.currentUser.id = 1
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'SCSO'
            return

        elif user=="AM" and password=="123":
            database.currentUser.id = 2
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'AM'
            return

        elif user=="FM" and password=="123":
            database.currentUser.id = 3
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'FM'
            return

        elif user=="SM" and password=="123":
            database.currentUser.id = 4
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'SM'
            return

        elif user=="PM" and password=="123":
            database.currentUser.id = 5
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'PM'
            return
        
        elif user=="HRTM" and password=="123":
            database.currentUser.id = 6
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'HRTM'
            return

        elif user=="STM" and password=="123":
            database.currentUser.id = 7
            database.currentUser.username = user
            database.currentUser.password = password
            database.currentUser.position = 'STM'
            return

        else:
            input("Wrong login try again u stopido")
    return

