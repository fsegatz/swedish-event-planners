from models.eventrequest import EventRequest_Control
from clear import clear 


class FinancialManagerView:
    def __init__(self):
        self.eventRequest_Control=EventRequest_Control()
        while True:
            clear()
            print("Financial Manager Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show Event Request to review")
            
            key = input()
            if (key=="0"): break
            elif (key=="1"): self.show_event_requests()
            elif (key=="test"):
                atributes=[69,"Skynet","Doomsday","nine billion human lifes", 100000, 2022-10-12, 3048-10-12, "Destruction!"]
                self.eventRequest_Control.create_event_request(atributes, assigned2="FM", status="Under review", feasibility_review="Good shit", financial_review="")
        return

    def show_event_requests(self):
        while True:
            clear()
            print("All event requests that are waiting on review")
            eventRequests=self.eventRequest_Control.get_event_request_for_user()
            print(*eventRequests)
            req_id=input("Press id of event request to review or [0] to go back: ")
            if req_id == "0": break
            elif req_id in eventRequests:
                key=input("Enter financial review or [0] to go back: ")
                if not key=="0": self.eventRequest_Control.add_review(id=req_id, review=key)
        return