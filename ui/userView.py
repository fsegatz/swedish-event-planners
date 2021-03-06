import database
from clear import clear

from models.staffrequest import StaffRequest_Control
from models.subteamtask import SubTeamTask_Control, SubTeamTask
from models.financialrequest import FinancialRequest_Control

class UserView:
    def print_username(self):
        print("Welcome ", database.currentUser.username.capitalize())
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

    def create_subteam_task(self):
        self.subTeamTask_Control = SubTeamTask_Control()
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
        
        subTeamTask = SubTeamTask(event_reference, task_description, priority, database.currentUser.username, assigned_to)
        self.subTeamTask_Control.append(subTeamTask)
        input("Subteam task request completed! Press enter to continue")
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
        print(" ",end="")
        print(*self.financialRequest_Control.get_str_financial_requests(),end="")
        input()

    def show_current_staff_requests(self): 
        self.staffRequest_Control=StaffRequest_Control()
        clear()
        print(" ",end="")
        print(*self.staffRequest_Control.get_str_staff_requests(),end="")
        input()
