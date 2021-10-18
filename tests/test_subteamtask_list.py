# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.subteamtask import *
import database

def main():
    database.initialize()
    database.currentUser.username="STM"
    loop_var = 5

    subTeamTask_Control = SubTeamTask_Control()
    for i in range(loop_var):
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, "Fabian", "STM"))
        subTeamTask_Control.append(SubTeamTask(i, "test", 1, "Fabian", "AM"))

    subTeamTask_Control.show_subteamtasks_for_currentuser()

    return

main()