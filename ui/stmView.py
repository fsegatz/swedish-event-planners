from models.user import User
from ui.userView import UserView
from clear import clear
from models.subteamtask import *

class SubTeamMemberView(UserView):
    def __init__(self):
        while(True):
            clear()
            self.print_username()
            print("SubTeam Member Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show SubTeamTasks List")

            key = input()
            if (key == '0'): break
            elif (key == '1'): self.start_subteamtask_dialog()

        return

    def start_subteamtask_dialog(self):
        subTeamTask_Control = SubTeamTask_Control()
        
        while (True):
            clear()
            subTeamTask_List = subTeamTask_Control.show_subteamtasks_for_currentuser()
            if(len(subTeamTask_List) == 0):
                print("[0] Return")
                key = input("Please choose option: ")
                if (key == '0'): break
            else:
                print("[0] Return")
                print("[1] Comment on subteam task")
                key = input("Please choose option: ")
                if (key == '0'): break
                elif (key == '1'): self.select_subteamtask_from_tasklist_to_comment(subTeamTask_List)
        return

    def select_subteamtask_from_tasklist_to_comment(self, tasklist):
        subTeamTask_Control = SubTeamTask_Control()

        clear()
        if(len(tasklist) == 0):
            return

        subTeamTask_Control.print_tasklist(tasklist)
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

    def change_subteamtask_comment_form(self, subTeamTask):
        subTeamTask_Control = SubTeamTask_Control()

        clear()

        subTeamTask_List = []
        subTeamTask_List.append(subTeamTask)
        subTeamTask_Control.print_tasklist(subTeamTask_List)

        print("Subteam task comment form.")
        while(True):
            comment = input("Please enter comment: ")
            if(self.verify_input()):
                break

        subTeamTask_Control.set_comment_of_subteamtask_with_id(subTeamTask.id, comment)
        return

    def verify_input(self):
        while(True):
            key = input("Is input correct? (y/n)")
            if (key.lower() == "y"):
                done = True
            elif (key.lower() == "n"):
                done = False
            else:
               print("Only valid priorities are y (Yes) and n (No)")
               continue 
            break
        return done