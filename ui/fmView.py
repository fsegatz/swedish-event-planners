import sys, os

testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventRequest import EventRequest_control
from clear import clear 


class FmView():
    def __init__(self):
        self.eventRequest_control=EventRequest_control()
        while True:
            key=self.start_view()
            
            if key=="1":
                self.show_event_requests()
            elif key=="2":
                return

            elif key=="test":
                atributes=[69,"Skynet","Doomsday","nine billion human lifes", 100000, 2022-10-12, 3048-10-12, "Destruction!"]
                self.eventRequest_control.create_eventRequest(atributes, assigned2="FM", status="Under review", feasibility_review="Good shit", financial_review="")
        
    def start_view(self):
        clear()
        print("Financial Manager Main View")
        print("------------------------")
        print("[1] Show Event Request to review")
        print("[2] Logout")
        return input()

    def show_event_requests(self):
        while True:

            clear()
            print("All event requests that are waiting on review")
            event_requests=self.eventRequest_control.get_event_request_for_user()
            print(*event_requests)
            req_id=input("Press id of event request to review or [0] to go back: ")
            if req_id == "0":break
            elif req_id in event_requests:
                key=input("Enter financial review or [0] to go back: ")
                if not key=="0": self.eventRequest_control.add_review(id=req_id, review=key)