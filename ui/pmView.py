from clear import clear
from models.eventplanning import EventPlanning_Control
from models.subteamtask import *

class ProductionManagerView():
    def __init__(self):
        while(True):
            clear()
            print("Production Manager Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Create subteam task")
            print("[2] Show current events")

            key = input("Please choose option: ")
            if(key == '0'): break
            if(key == '1'): self.create_subteam_task()
            if(key == '2'): self.show_current_events()
            
        return

    def create_subteam_task(self):
        clear()
        subTeamTask_Control = SubTeamTask_Control()
        subTeamTask_Control.create_subteamtask_form()

    def show_current_events(self):
        clear()
        eventPlanning_Control = EventPlanning_Control()
        eventPlanning_Control.show_current_eventplannings()
        input('Press enter to return') #temporary before adding functionality