import sys, os

testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventRequest import EventRequest_control
from clear import clear 
import database

def scso_view():
    while True:
        clear()
        print("Senior Customer Support Officer Main View")
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
                key=input("Press id of event request to review or [0] to go back: ")
                if key == "0":break

        elif key=="2":
            return
            
        elif key=="test":
            atributes=[database.id_counter.get_new(),"Skynet","Doomsday","nine billion", 100000, 2022-10-12, 3048-10-12, "Destruction!", "Open"]
            try:eventRequest_control
            except:eventRequest_control=EventRequest_control()
            eventRequest_control.create_eventRequest(atributes)
    return 