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
            tasklist = subTeamTask_Control.show_subteamtasks_for_currentuser()
            if(len(tasklist) == 0):
                print("[0] Return")
                key = input("Please choose option: ")
                if (key == '0'): break
            else:
                print("[0] Return")
                print("[1] Comment on subteam task")
                key = input("Please choose option: ")
                if (key == '0'): break
                elif (key == '1'): subTeamTask_Control.select_subteamtask_from_tasklist_to_comment(tasklist)
        return