from ui.login import *
from ui.mainView import mainView

from models.user import *

import database

def main():
    database.initialize()
    while(True):
        login()
        mainView()

main()

