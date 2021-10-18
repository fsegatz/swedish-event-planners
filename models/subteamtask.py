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

class SubTeamTask_Control:
    def __init__(self):
        pass

    def append(self, subTeamTask):
        length = len(database.subTeamTask_List)
        if (length == 0):
            subTeamTask.id = 1
        else:
            subTeamTask.id = database.subTeamTask_List[length-1].id + 1
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
                " |")
        return

    def get_subteamtasks_for_user(self, user):
        tasklist = []
        for index, ref in enumerate(database.subTeamTask_List):
            subTeamTask = database.subTeamTask_List[index]
            if (subTeamTask.assigned_to == user.username):
                tasklist.append(subTeamTask)
        return tasklist

    def show_subteamtasks_for_currentuser(self):
        tasklist = self.get_subteamtasks_for_user(database.currentUser)
        self.print_tasklist(tasklist)

    def create_subteamtask_form(self):
        clear()
        print("Please enter folowing subteam task details")
        event_reference = input("Event reference: ")
        task_description = input("Description: ")
        assigned_to = input("Assign to: ")

        while (True):
            priority = input("Priority (low, medium, high): ")
            if (priority.lower() == "low"):
                priority = 1
            elif (priority.lower() == "medium"):
                priority = 2
            elif (priority.lower() == "high"):
                priority = 3
            else:
                print("Only valid priorities are low, medium and high")
                continue
            break
        
        input("Subteam task request completed! Press enter to send task")
        subteamTask = SubTeamTask(event_reference, task_description, priority, database.currentUser.username, assigned_to)
        database.subTeamTask_List.append(subteamTask)

        return subteamTask


        
