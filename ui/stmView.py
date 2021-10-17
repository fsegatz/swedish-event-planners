from clear import clear
from models.subteamtask import *
import time

def stm_view():
    stay=1
    while(stay):
        clear()
        print("SubTeam Member Main View")
        print("------------------------")
        print("[0] Logout")
        print("[1] Show SubTeamTasks List")
        option = input("Please choose option: ")
        if(option == '0'):
            stay = 0
        if(option == '1'):
            clear()
            subTeamTask_Control = SubTeamTask_Control()
            subTeamTask_Control.show_subteamtasks_for_currentuser()
            time.sleep(5) # Placeholder until filled with real functionalities to interact with list
    return