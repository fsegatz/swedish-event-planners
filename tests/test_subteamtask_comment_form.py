# User Story
#  "Any subteam member should be able to access a form similar to the subteam task form. This form should allow them to write a comment to the task."

from datetime import datetime

# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.subteamtask import *
import database

def main():
    database.initialize()

    subTeamTask_Control = SubTeamTask_Control()

    # Create a view subteam tasks from PM
    database.currentUser.username="PM"
    for i in range(5):
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, database.currentUser.username, "STM"))
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, database.currentUser.username, "AM"))

    # Login as subteam member and change to a task
    database.currentUser.username="STM"
    tasklist = subTeamTask_Control.show_subteamtasks_for_currentuser()
    
    subTeamTask = tasklist[1]
    subTeamTask_Control.change_subteamtask_comment_form(subTeamTask)

    # login as user who subteamtask was assigned to
    database.currentUser.username = subTeamTask.assigned_to
    print("\nLogin as user who subteamtak was assigned to: ", database.currentUser.username, "\n")
    subTeamTask_Control.show_subteamtasks_for_currentuser()
    
    return
    
main()