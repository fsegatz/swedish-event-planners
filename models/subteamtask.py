from sys import dont_write_bytecode
import database
from clear import clear
from datetime import datetime

class SubTeamTask:
    def __init__(self, event_reference, task_description, task_priority, assigned_by, assigned_to):
        self.id = ""
        self.event_reference = event_reference
        self.creation_date=datetime.now()
        self.task_description=task_description
        self.priority=task_priority
        self.assigned_by=assigned_by
        self.assigned_to=assigned_to
        self.comment= ""
        self.status= "new"      #<--status can be [new; commented]
        return

class SubTeamTask_Control:
    def __init__(self):
        return

    def append(self, subTeamTask):
        subTeamTask.id = database.id_counter.get_new()
        database.subTeamTask_List.append(subTeamTask)
        return

    def print_list(self):
        for index, ref in enumerate(database.subTeamTask_List):
            subTeamTask = database.subTeamTask_List[index]
            print(
                "|Index: ", index,
                "|Creation date: ", subTeamTask.creation_date,
                "|Created by: ", subTeamTask.assigned_by,
                "|Assigned to: ", subTeamTask.assigned_to,
                "|Event ref id: ", subTeamTask.event_reference,
                "|")
        return

    def print_tasklist(self, tasklist):
        print("My Tasks")
        if (len(tasklist) == 0):
            print("No Tasks available") 
        for index, ref in enumerate(tasklist):
            subTeamTask = tasklist[index]
            print(
                "[", index, "] "
                " | Event reference: ", subTeamTask.event_reference,
                " | Priority: ", subTeamTask.priority,
                " | Assigned by: ", subTeamTask.assigned_by,
                " | Task description: ", subTeamTask.task_description,
                " | Comment: ", subTeamTask.comment,
                " |")
        print("")
        return

    def get_subteamtasks_for_user(self, user): return [subTeamTask for subTeamTask in database.subTeamTask_List if subTeamTask and subTeamTask.assigned_to == user.username]
    def get_subteamtasks_for_currentuser(self): return self.get_subteamtasks_for_user(database.currentUser)

    def show_subteamtasks_for_currentuser(self):
        tasklist = self.get_subteamtasks_for_currentuser()
        self.print_tasklist(tasklist)
        return tasklist