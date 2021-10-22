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
            try:eventRequest_control
            except:eventRequest_control=EventRequest_control()
            eventRequest_control.show_event_request_for_user()

        elif key=="2":
            return
    return