import sys, os

testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventRequest import EventRequest_control
from clear import clear 

def am_view():
    while True:
        clear()
        print("Administration Manager Main View")
        print("------------------------")
        print("[1] Show Event Request to finalize/reject")
        print("[2] Logout")
        key=input()
        
        if key=="1":
            while True:
                try:eventRequest_control
                except:eventRequest_control=EventRequest_control()

                clear()
                print("All event requests that are waiting on finalize/reject")
                event_requests=eventRequest_control.get_event_request_for_user()
                print(*event_requests)
                req_id=input("Press id of event request to finalize/reject or [0] to go back: ")

                if req_id == "0":break
                elif req_id in event_requests:

                    clear()
                    print("Event request " + req_id )
                    feasabilty_review, financial_review = eventRequest_control.get_reviews_from_event_request(id=req_id)
                    print("Financial review: " + financial_review)
                    print("")
                    print("[1] Finalize event request")
                    print("[2] Reject event request")
                    print("[0] Go back")
                    key=input("")

                    if key=="0":pass
                    elif key=="1": eventRequest_control.finalize_event_request(id=req_id)
                    elif key=="2":
                        clear()
                        print("Are you sure that you want reject event request " + req_id + " it will not be possible to get back")
                        print("[1] Yes, reject this event request")
                        print("[2] No, do not reject")
                        key=input("")
                        if key=="1": eventRequest_control.reject_event_request(id=req_id)
                    
        elif key=="2": return
        elif key=="test":
            atributes=[69,"Skynet","Doomsday","nine billion human lifes", 100000, 2022-10-12, 3048-10-12, "Destruction!"]
            try:eventRequest_control
            except:eventRequest_control=EventRequest_control()
            eventRequest_control.create_eventRequest(atributes, assigned2="AM", status="Under review", feasibility_review="Good shit", financial_review="Noice!")
    return