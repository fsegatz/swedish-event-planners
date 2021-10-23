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

class SubTeamTask_Control:
    def __init__(self):
        pass

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
        return tasklist

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
        subTeamTask = SubTeamTask(event_reference, task_description, priority, database.currentUser.username, assigned_to)
        database.subTeamTask_List.append(subTeamTask)

        return subTeamTask

    def change_subteamtask_comment_form(self, subTeamTask):
        #search for subteamtask in db with same id
        for index, ref in enumerate(database.subTeamTask_List):
            buf = database.subTeamTask_List[index]
            if (subTeamTask.id == buf.id):
                break

        clear()
        print("Subteam task comment form.")
        while(True):
            database.subTeamTask_List[index].comment = input("Please enter comment: ")
            while(True):
                done = input("Is comment correct? (y/n)")
                if (done.lower() == "y"):
                    done = "y"
                elif (done.lower() == "n"):
                    done = "n"
                else:
                   print("Only valid priorities are y (Yes) and n (No)")
                   continue 
                break
            if(done == "n"):
                continue
            break
        database.subTeamTask_List[index].status == "commented"
        return

    def select_subteamtask_from_tasklist_to_comment(self, tasklist):
        clear()
        if(len(tasklist) == 0):
            return

        self.print_tasklist(tasklist)
        while(True):
            index = input("Enter index of subteam task that should be commented, or c to cancel: ")
            if(index.lower() == 'c'):
                return 
            elif (index.isnumeric()):
                if(int(index) < len(tasklist) ):
                    subTeamTask = tasklist[int(index)]
                    self.change_subteamtask_comment_form(subTeamTask)
                else:
                    print("Index is out of bound")
                    continue
            else:
                print("No valid input")
                continue
            break
        return subTeamTask