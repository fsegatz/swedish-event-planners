from ui.login import *
from ui.mainView import mainView

from models.user import *

import database

def main():
    database.initialize()
    user_Control = User_Control()
    user_Control.fill_user_database()

    while(True):
        login_dialog()
        mainView()

main()

