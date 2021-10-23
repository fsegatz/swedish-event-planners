from clear import clear
from models.eventplanning import EventPlanning_Control
from models.staffrequest import StaffRequest_Control
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
            elif(key == '1'): self.create_subteam_task()
            elif(key == '2'): self.show_current_events()
            elif (key== "3"): self.create_staff_request()

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
    
    def create_staff_request(self):
        self.staffRequest_Control=StaffRequest_Control()
        clear()
        print("Please enter folowing staff recruitment details")
        contract_type = input("Contract type (Full time / Part time): ")
        while not contract_type in ["Full time", "Part time"]:
            contract_type = input("Contract type must be Full time or Part time: ")
        requesting_department = input("Requesting department: ")
        years_of_experience = input("Years of experience: ")
        job_title = input("Job title: ")
        job_description = input("Job description: ")
        status = "opened"

        atributes=[contract_type, requesting_department, years_of_experience, job_title, job_description, status]
        self.staffRequest_Control.create_staff_request(atributes)
        input("Event request completed! Press enter to continue")