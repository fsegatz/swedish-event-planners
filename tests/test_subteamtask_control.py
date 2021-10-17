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

    subTeamTask_list_length = len(database.subTeamTask_List)
    subTeamTask_Control = SubTeamTask_Control()

    for i in range(5):
        event_reference = 0
        task_description = "This is a task description"
        task_priority = 1
        assigned_by = "currentUser"
        assigned_to = "User xy"
        subTeamTask_Control.append(SubTeamTask(event_reference, datetime.now(), task_description, task_priority, assigned_by, assigned_to))

    if (subTeamTask_list_length != len(database.subTeamTask_List)):
        print("test: length of subTeamTask_list changed")
    
    subTeamTask_Control.print_list()
    return

main()