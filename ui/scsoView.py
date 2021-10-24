from ui.userView import UserView
from models.eventrequest import EventRequest_Control
from models.eventplanning import *
from clear import clear 

class SeniorCustomerServiceOfficerView(UserView):
    def __init__(self):
        self.eventRequest_Control=EventRequest_Control()
        self.eventPlanning_Control=EventPlanning_Control()

        while True:
            clear()
            self.print_username()
            print("Senior Customer Service Officer Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show Event Request to review")
            print("[2] Create event plan from event request")

            key = input()
            if (key=="0"): break
            elif (key=="1"): self.show_event_requests()
            elif (key=="2"): self.create_event_plan()

            elif (key=="test"):
                atributes=["69","Skynet","Doomsday","nine billion human lifes", "100000", "2022-10-12", "3048-10-12", "Destruction!"]
                self.eventRequest_Control.create_event_request(atributes)
        return

    def show_event_requests(self):
        while True:
            clear()
            print("All event requests that are waiting on review")
            print(" ",end="")
            print(*self.eventRequest_Control.get_event_request_for_user())

            req_id=input("Press id of event request to review or [0] to go back: ")
            if req_id == "0":break
            elif req_id in self.eventRequest_Control.get_id_of_event_request_for_user():
                clear()
                print(self.eventRequest_Control.get_reviews_from_event_request(id=req_id))
                key=input("\nEnter feasbilty review or [0] to go back: \n")
                if not key=="0":self.eventRequest_Control.add_review(id=req_id, review=key)
        return

    def create_event_plan(self):
        while True:
            clear()
            print("All finalized event requests")
            eventRequests=self.eventRequest_Control.get_finalized_event_request()
            print(*eventRequests)

            req_id=input("Press id of event request to create event plan from or press [0] to go back: ")
            if req_id == "0": break
            elif req_id in eventRequests:
                clear()
                print("Are you sure that you want to create event plan from event request " + req_id + " it will not be possible to undo")
                print("[1] Yes, create event plan")
                print("[2] No, go back")

                key=input("")
                if (key=="1"):
                    event_request_data=self.eventRequest_Control.get_info_for_event_plan(id=req_id)
                    self.eventRequest_Control.archived_event_request(id=req_id)

                    eventPlanning=EventPlanning(event_request_data[0], event_request_data[1], event_request_data[2], event_request_data[3], event_request_data[4], event_request_data[5], event_request_data[6], event_request_data[7])
                    self.eventPlanning_Control.append(eventPlanning)
        return