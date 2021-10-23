from models.eventrequest import EventRequest_control
from models.eventplanning import *
from clear import clear 

class SeniorCustomerServiceOfficerView:
    def __init__(self):
        self.eventRequest_control=EventRequest_control()
        self.eventPlanning_Control=EventPlanning_Control()

        while True:
            clear()
            print("Senior Customer Support Officer Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show Event Request to review")
            print("[2] Create event plan from event request")

            key = input()
            if (key=="0"): break
            elif (key=="1"): self.show_event_requests()
            elif (key=="2"): self.create_event_plan()

            elif (key=="test"):
                atributes=[69,"Skynet","Doomsday","nine billion human lifes", 100000, 2022-10-12, 3048-10-12, "Destruction!"]
                self.eventRequest_control.create_eventRequest(atributes)
        return

    def show_event_requests(self):
        while True:
            clear()
            print("All event requests that are waiting on review")
            event_requests=self.eventRequest_control.get_event_request_for_user()
            print(*event_requests)

            req_id=input("Press id of event request to review or [0] to go back: ")
            if req_id == "0":break
            elif req_id in event_requests:
                key=input("Enter feasbilty review or [0] to go back: ")
                if not key=="0":self.eventRequest_control.add_review(id=req_id, review=key)
        return

    def create_event_plan(self):
        while True:
            clear()
            print("All finalized event requests")
            event_requests=self.eventRequest_control.get_finalized_event_request()
            print(*event_requests)

            req_id=input("Press id of event request to create event plan from or press [0] to go back: ")
            if req_id == "0": break
            elif req_id in event_requests:
                clear()
                print("Are you sure that you want to create event plan from event request " + req_id + " it will not be possible to undo")
                print("[1] Yes, create event plan")
                print("[2] No, go back")

                key=input("")
                if (key=="1"):
                    event_request_data=self.eventRequest_control.get_info_for_event_plan(id=req_id)
                    self.eventRequest_control.archived_event_request(id=req_id)

                    eventplanning=EventPlanning(event_request_data[0], event_request_data[1], event_request_data[2], event_request_data[3], event_request_data[4], event_request_data[5], event_request_data[6], event_request_data[7])
                    self.eventPlanning_Control.append(eventplanning)
        return