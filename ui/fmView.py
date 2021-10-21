import sys, os

testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventRequest import EventRequest_control
from clear import clear 

def fm_view():
    while True:
        clear()
        print("Financial Manager Main View")
        print("------------------------")
        print("[1] Show Event Request to review")
        print("[2] Logout")
        key=input()
        
        if key=="1":
            while True:
                try:eventRequest_control
                except:eventRequest_control=EventRequest_control()

                clear()
                print("All event requests that are waiting on review")
                event_requests=eventRequest_control.get_event_request_for_user()
                print(*event_requests)
                req_id=input("Press id of event request to review or [0] to go back: ")
                if req_id == "0":break
                elif req_id in event_requests:
                    key=input("Enter financial review or [0] to go back: ")
                    if key=="0":pass
                    else:eventRequest_control.add_review(id=req_id, review=key)
                    


        elif key=="2":
            return
    return