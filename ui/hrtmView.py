from ui.userView import UserView
from models.staffrequest import StaffRequest_Control
from models.staffrequest import StaffRequest
from clear import clear
import database

class HumanResourceTeamMemberView(UserView):
    def __init__(self):
        self.staffRequest_Control= StaffRequest_Control()
        
        while(True):
            clear()
            self.print_username()
            print("Human Resource Team Member Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show current staff requests")

            
            key = input("Please choose key: ")
            if (key == '0'): break
            elif (key == '1'): self.show_current_staff_requests()
            elif(key=="test"):
                atributes=["Full time", "Decoration" , "4" , "Table fixer" , "fix tables to make them look nice", "opened"]
                req=StaffRequest(database.id_counter.get_new(),atributes)
                database.staffRequest_List.append(req)
        return
    
    def show_current_staff_requests(self): 
        self.staffRequest_Control=StaffRequest_Control()
        while True:
            clear()
            print("All staff requests that are waiting on review")
            print(" ",end="")
            print(*self.staffRequest_Control.get_str_staff_requests())

            req_id=input("Press id of staff request to review or [0] to go back: ")
            if req_id == "0": break
            elif req_id in self.staffRequest_Control.get_id_of_staff_request_for_user():
                clear()
                print(self.staffRequest_Control.get_str_staff_request_from_id(id=req_id))

                key=input("\nChange staff request status (Opened/Rejected/In progress/Archived) or [0] to go back: \n")
                while key not in ["Opened", "Rejected", "In progress" ,"Archived" , "0"]:
                    clear()
                    print(self.staffRequest_Control.get_str_staff_request_from_id(id=req_id))
                    print("Unvalid input, valid inputs are Opened, Rejected, In progress or Archived")
                    key=input("\nPlease enter valid input or [0] to go back: \n")
                if not key=="0": self.staffRequest_Control.add_status(id=req_id, status=key)
        return
        

