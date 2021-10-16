# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.subteamtask import *

subTeamTask_List = []

class SubTeamTask_Control:
    def append(self, subTeamTask):
        subTeamTask_List.append(subTeamTask)
        return

def main():
    subTeamTask_Control = SubTeamTask_Control()

    event_reference = 0
    creation_date = 0
    task_description = "This is a task description"
    task_priority = 1
    assigned_by = "currentUser"
    assigned_to = "User xy"
    
    new_subteamtask = SubTeamTask(event_reference, creation_date, task_description, task_priority, assigned_by, assigned_to)

    subTeamTask_Control.append(new_subteamtask)
    
    
    return

main()