from datetime import datetime

# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.subteamtask import *

def main():
    event_reference = 0
    creation_date = datetime.now()
    task_description = "This is a task description"
    task_priority = 1
    assigned_by = "currentUser"
    assigned_to = "User xy"
    subTeamTask = SubTeamTask(event_reference, creation_date, task_description, task_priority, assigned_by, assigned_to)

    if( subTeamTask.event_reference == event_reference):
        print(subTeamTask.creation_date, ": Subtask was created")
    else:
        print("Subtask Instanciation doesn't work")

    return

main()