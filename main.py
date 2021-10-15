from ui.login import *
from models.user import *
import database

#currentUser = User(0, 'default', 'default', 'default')

def main():
    database.initialize()
    login()
    print(database.currentUser.position)
    if database.currentUser.position=='CSO':
        print("it worked!")
    else:
        print("did not work")
    return

main()

