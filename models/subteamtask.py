from sys import dont_write_bytecode
import database

class SubTeamTask:
    def __init__(self, event_reference, creation_date, task_description, task_priority, assigned_by, assigned_to):
        self.id = ""
        self.event_reference = event_reference
        self.creation_date=creation_date
        self.task_description=task_description
        self.posittask_priorityion=task_priority
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

    def print_list(self):
        length = len(database.subTeamTask_List)
        while(length):
            length -= 1
            subTeamTask = database.subTeamTask_List[length]
            print(
                "|ID: ", subTeamTask.id,
                "|Index: ", length,
                "|Creation date: ", subTeamTask.creation_date,
                "|Created by: ", subTeamTask.assigned_by,
                "|Assigned to: ", subTeamTask.assigned_to,
                "|Event ref id: ", subTeamTask.event_reference,
                "|")

    def showItemsForUser(self, user):
        tasklist = []
        length = len(database.subTeamTask_List)
        while(length):
            length -= 1
            subTeamTask = database.subTeamTask_List[length]
            if (subTeamTask.assigned_to == user.username):
                tasklist.append(subTeamTask)
                
        return tasklist

