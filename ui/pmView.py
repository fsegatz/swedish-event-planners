from clear import clear
from models.eventplanning import EventPlanning_Control
from models.staffrequest import StaffRequest_Control
from models.financialrequest import FinancialRequest_Control
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
            print("[3] Create staff request")
            print("[4] Create financial request")
            print("[5] Show current financial request")

            key = input("Please choose option: ")
            if(key == '0'): break
            elif(key == '1'): self.create_subteam_task()
            elif(key == '2'): self.show_current_events()
            elif (key== "3"): self.create_staff_request()
            elif key == "4": self.create_financial_request()
            elif key == "5": self.show_current_financial_requests()

        return

    def create_subteam_task(self):
        clear()
        subTeamTask_Control = SubTeamTask_Control()
        subTeamTask_Control.create_subteamtask_form()
        return

    def show_current_events(self):
        eventPlanning_Control = EventPlanning_Control()
        eventPlanning_Control.show_current_eventplannings()
        
        while (True):
            clear()
            eventPlanningsList = eventPlanning_Control.show_current_eventplannings()
            if(len(eventPlanningsList) == 0):
                print("[0] Return")
                key = input("Please choose option: ")
                if (key == '0'): break
            else:
                print("[0] Return")
                print("[1] Edit event info")
                key = input("Please choose option: ")
                if (key == '0'): break
                elif (key == '1'): 
                    eventPlanning = eventPlanning_Control.event_planning_select_from_list(eventPlanningsList)
                    eventPlanning = eventPlanning_Control.event_planning_info_edit_dialog(eventPlanning)
        return

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
        return

    def create_financial_request(self):
        self.financialRequest_Control=FinancialRequest_Control()
        clear()
        print("Please enter folowing financial request details")

        event_reference = input("Event reference: ") #do some check if there is event with that id and loop
        requesting_department = input("Requesting department: ")
        required_amount = input("Required amount: ")
        reason = input("Reason: ")
        comment = input("Comment: ")
        status = "opened"

        atributes=[event_reference, requesting_department, required_amount, reason, comment, status]
        self.financialRequest_Control.create_financial_request(atributes)
        input("Financial request completed! Press enter to continue")

    def show_current_financial_requests(self): 
        self.financialRequest_Control=FinancialRequest_Control()
        clear()
        print(*self.financialRequest_Control.get_str_financial_requests(),end="")
        input()