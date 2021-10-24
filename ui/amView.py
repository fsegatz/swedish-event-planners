from ui.userView import UserView
from models.eventrequest import EventRequest_Control
from clear import clear 

class AdministrationManagerView(UserView):
    def __init__(self):
        self.eventRequest_Control=EventRequest_Control()
        while True:
            clear()
            self.print_username()
            print("Administration Manager Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Show Event Request to finalize/reject")
            
            key=input()
            if (key=="0"): break
            elif (key=="1"): self.show_event_request_to_finalize()
            elif (key=="test"):
                atributes=["69","Skynet","Doomsday","nine billion human lifes", "100000", "2022-10-12", "3048-10-12", "Destruction!"]
                self.eventRequest_Control.create_event_request(atributes, assigned2="AM", status="Under review", feasibility_review="Good shit", financial_review="Noice!")
        return

    def show_event_request_to_finalize(self):
        while True:

            clear()
            print("All event requests that are waiting on finalize/reject")
            print(" ",end="")
            print(*self.eventRequest_Control.get_event_request_for_user())

            req_id=input("Press id of event request to finalize/reject or [0] to go back: ")
            if req_id == "0": break

            elif req_id in self.eventRequest_Control.get_id_of_event_request_for_user():
                while True:
                    key = self.finalize_or_reject_view(req_id)
                    if (not self.verify_input()): continue
                    if (key=="0"): pass
                    elif (key=="1"): self.eventRequest_Control.finalize_event_request(id=req_id)
                    elif (key=="2"): self.eventRequest_Control.reject_event_request(id=req_id)
                    else: continue
                    break
        return

    def finalize_or_reject_view(self,req_id):
        clear()
        print(self.eventRequest_Control.get_reviews_from_event_request(id=req_id))
        print("")
        print("[0] Go back")
        print("[1] Finalize event request")
        print("[2] Reject event request")
        return input("")

    # def reject_confirm(self,req_id):
    #     clear()
    #     print("Are you sure that you want reject event request " + req_id + " it will not be possible to get back")
    #     print("[1] Yes, reject this event request")
    #     print("[2] No, do not reject")
    #     return input("")