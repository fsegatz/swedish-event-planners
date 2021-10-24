# User Story
#  "Any subteam member should be able to access a form similar to the subteam task form. This form should allow them to write a comment to the task."

# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.subteamtask import *
from models.user import *
from ui.stmView import *
import database

def main():
    database.initialize()
    user_Control = User_Control()
    user_Control.fill_user_database()

    subTeamTask_Control = SubTeamTask_Control()
    subTeamMemberView = SubTeamMemberView()

    # Create a view subteam tasks from PM
    user_Control.login('PM', '123')

    for i in range(5):
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, database.currentUser.username, "STM"))
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, database.currentUser.username, "AM"))

    # Login as subteam member and change to a task
    user_Control.login('STM', '123')
    tasklist = subTeamTask_Control.show_subteamtasks_for_currentuser()

    subTeamTask = subTeamMemberView.select_subteamtask_from_tasklist_to_comment(tasklist)

    if (subTeamTask != None):
        print("\nLogin as user who subteamtak was assigned to: ", database.currentUser.username, "\n")
        subTeamTask_Control.show_subteamtasks_for_currentuser()
        
    return
    
main()