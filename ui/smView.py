from clear import clear
from models.subteamtask import *
from models.eventplanning import *
import time

class ServiceManagerView:
    def __init__(self):
        self.subTeamTask_Control = SubTeamTask_Control()
        self.eventPlanning_Control = EventPlanning_Control()
        
        while(True):
            clear()
            print("Service Manager Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Create subteam task")
            print("[2] Show current events")
            
            key = input("Please choose key: ")
            if (key == '0'): break
            elif (key == '1'): self.create_subteam_task()
            elif (key == '2'): self.show_current_events()

        return

    def create_subteam_task(self):
        clear()
        self.subTeamTask_Control.create_subteamtask_form()

    def show_current_events(self):
        clear()
        self.eventPlanning_Control.show_current_eventplannings()
        input('Press enter to return') #temporary before adding functionality

