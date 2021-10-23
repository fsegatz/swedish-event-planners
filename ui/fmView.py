from models.financialrequest import FinancialRequest_Control
from models.eventrequest import EventRequest_Control
from ui.userView import UserView
from models.user import User
from clear import clear 


class FinancialManagerView(UserView):
    def __init__(self):
        self.eventRequest_Control=EventRequest_Control()
        while True:
            clear()
            self.print_username()
            print("Financial Manager Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show Event Request to review")
            print("[2] Show current financial request")
            
            key = input()
            if (key=="0"): break
            elif (key=="1"): self.show_event_requests()
            elif key == "2": self.show_current_financial_requests()
            elif (key=="test"):
                atributes=["69","Skynet","Doomsday","nine billion human lifes", "100000", "2022-10-12", "3048-10-12", "Destruction!"]
                self.eventRequest_Control.create_event_request(atributes, assigned2="FM", status="Under review", feasibility_review="Good shit", financial_review="")
        return

    def show_event_requests(self):
        while True:
            clear()
            print("All event requests that are waiting on review")
            print(*self.eventRequest_Control.get_event_request_for_user())

            req_id=input("Press id of event request to review or [0] to go back: ")
            if req_id == "0": break
            elif req_id in self.eventRequest_Control.get_id_of_event_request_for_user():
                clear()
                print(self.eventRequest_Control.get_reviews_from_event_request(id=req_id))
                key=input("\nEnter financial review or [0] to go back: \n")
                if not key=="0": self.eventRequest_Control.add_review(id=req_id, review=key)
        return

    def show_current_financial_requests(self): 
        self.financialRequest_Control=FinancialRequest_Control()
        while True:
            clear()
            print("All financial requests that are waiting on review")
            print(*self.financialRequest_Control.get_str_financial_requests())

            req_id=input("Press id of financial request to review or [0] to go back: ")
            if req_id == "0": break
            elif req_id in self.financialRequest_Control.get_id_of_financial_request_for_user():
                clear()
                print(self.financialRequest_Control.get_str_financial_request_from_id(id=req_id))
                key=input("\nEnter financial review or [0] to go back: \n")
                if not key=="0": self.financialRequest_Control.add_review(id=req_id, review=key)
        return

