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
        clear()
        print(*self.staffRequest_Control.get_current_staff_request(),end="")
        input()
        
