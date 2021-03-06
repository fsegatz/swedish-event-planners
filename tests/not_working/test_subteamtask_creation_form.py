# User Story
#  "A ProductionManager and ServiceManager should be able to create subteam tasks through a form."

## !!! Not working anymore !!! ##

from datetime import datetime

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
    user_Control.login("PM", "123")

    subTeamTask_Control = SubTeamTask_Control()

    subTeamTask = subTeamTask_Control.create_subteamtask_form()

    # login as user who subteamtask was assigned to
    user_Control.login(subTeamTask.assigned_to, "123")
    print("\nLogin as user who subteamtak was assigned to: ", database.currentUser.username, "\n")
    subTeamTask_Control.show_subteamtasks_for_currentuser()
    
    return
    
main()