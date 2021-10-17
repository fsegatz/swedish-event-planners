from sys import dont_write_bytecode
import database

class SubTeamTask:
    def __init__(self, event_reference, creation_date, task_description, task_priority, assigned_by, assigned_to):
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
        database.subTeamTask_List.append(subTeamTask)
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
