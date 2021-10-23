from clear import clear
from models.user import *

def login_dialog():
    user_Control = User_Control()
    wrong_login = False
    while (True):
        clear()
        if(wrong_login):
            print("Wrong login. Try again.")
            wrong_login = False
        
        username=input("Enter username: ")
        password=input("Enter password: (pssst its 123)  ")
        
        if(user_Control.login(username, password)): break
        else: wrong_login = True

    return