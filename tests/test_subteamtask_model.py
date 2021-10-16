from datetime import datetime

class SubTeamTask():
    def __init__(self, event_reference, creation_date, task_description, task_priority, assigned_by, assigned_to):
        self.event_reference = event_reference
        self.creation_date=creation_date
        self.task_description=task_description
        self.posittask_priorityion=task_priority
        self.assigned_by=assigned_by
        self.assigned_to=assigned_to

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