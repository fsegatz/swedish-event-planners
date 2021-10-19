from clear import clear
from models.subteamtask import *
import time

def stm_view():
    while(True):
        clear()
        print("SubTeam Member Main View")
        print("------------------------")
        print("[0] Logout")
        print("[1] Show SubTeamTasks List")
        option = input("Please choose option: ")
        if(option == '0'):
            break
        elif(option == '1'):
            subTeamTask_Control = SubTeamTask_Control()
            while (True):
                clear()
                tasklist = subTeamTask_Control.show_subteamtasks_for_currentuser()
                if(len(tasklist) != 0):
                    print("[0] Return")
                    print("[1] Comment on subteam task")
                    option = input("Please choose option: ")
                    if(option == '0'):
                        break
                    elif(option == '1'):
                        subTeamTask_Control.select_subteamtask_from_tasklist_to_comment(tasklist)
                    else:
                        pass
                    continue
                else: 
                    print("[0] Return")
                    option = input("Please choose option: ")
                    if(option == '0'):
                        break
                    else:
                        continue
            continue
    return