from models.eventrequest import EventRequest_control
from clear import clear 

class AdministrationManagerView:
    def __init__(self):
        self.eventRequest_control=EventRequest_control()
        while True:
            clear()
            print("Administration Manager Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show Event Request to finalize/reject")
            
            key=input()
            if (key=="0"): break
            elif (key=="1"): self.show_event_request_to_finalize()
            elif (key=="test"):
                atributes=[69,"Skynet","Doomsday","nine billion human lifes", 100000, 2022-10-12, 3048-10-12, "Destruction!"]
                self.eventRequest_control.create_eventRequest(atributes, assigned2="AM", status="Under review", feasibility_review="Good shit", financial_review="Noice!")
        return

    def show_event_request_to_finalize(self):
         while True:

            clear()
            print("All event requests that are waiting on finalize/reject")
            event_requests=self.eventRequest_control.get_event_request_for_user()
            print(*event_requests)
            req_id=input("Press id of event request to finalize/reject or [0] to go back: ")
            if req_id == "0":break
            elif req_id in event_requests:
                while True:
                    key = self.finalize_or_reject_view(req_id)
                    if (key=="0"): pass
                    elif (key=="1"): 
                        self.eventRequest_control.finalize_event_request(id=req_id)
                    elif (key=="2"):
                        key=self.reject_confirm(req_id)
                        if (key=="1"): self.eventRequest_control.reject_event_request(id=req_id)
                    else: continue
                    break

    def finalize_or_reject_view(self,req_id):
        clear()
        print("Event request " + req_id )
        feasabilty_review, financial_review = self.eventRequest_control.get_reviews_from_event_request(id=req_id)
        print("Financial review: " + financial_review)
        print("")
        print("[0] Go back")
        print("[1] Finalize event request")
        print("[2] Reject event request")
        return input("")

    def reject_confirm(self,req_id):
        clear()
        print("Are you sure that you want reject event request " + req_id + " it will not be possible to get back")
        print("[1] Yes, reject this event request")
        print("[2] No, do not reject")
        return input("")