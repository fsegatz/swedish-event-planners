from clear import clear
from models.eventplanning import EventPlanning_Control
from models.subteamtask import *
import time

def pm_view():
    while(True):
        clear()
        print("Production Manager Main View")
        print("------------------------")
        print("[0] Logout")
        print("[1] Create subteam task")
        print("[2] Show current events")
        option = input("Please choose option: ")
        if(option == '0'):
            break
        if(option == '1'):
            clear()
            subTeamTask_Control = SubTeamTask_Control()
            tmp = subTeamTask_Control.create_subteamtask_form()
        if(option == '2'):
            clear()
            eventPlanning_Control = EventPlanning_Control()
            tmp = eventPlanning_Control.show_current_eventplannings()
            input('Press enter to return') #temporary before adding functionality
    return