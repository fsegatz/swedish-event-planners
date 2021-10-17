import sys, os

from models.eventRequest import EventRequest_control
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

import database
from clear import clear
Id=1

def cso_view():
    while True:
        clear()
        key=input("\
            Customer Support Officer Main View\n\
            ------------------------\n\
            [1] Create Event Request \n\
            [2] Logout\n")

        if key=="1":
            try:
                eventRequest_control.create_eventRequest()
            except:
                eventRequest_control=EventRequest_control()
                eventRequest_control.create_eventRequest()
        elif key=="2":
            return
    return 