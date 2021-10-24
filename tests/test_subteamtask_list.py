# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.user import User_Control
from models.subteamtask import *
import database

def main():
    database.initialize()
    user_Control = User_Control()
    user_Control.fill_user_database()   
    user_Control.login("STM", "123")


    subTeamTask_Control = SubTeamTask_Control()
    for i in range(5):
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, "Fabian", "STM"))
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, "Fabian", "AM"))

    subTeamTask_Control.show_subteamtasks_for_currentuser()

    return

main()