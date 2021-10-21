import sys, os

from models.eventRequest import EventRequest_control
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))


from clear import clear

def cso_view():
    while True:
        clear()
        key=input("\
Customer Support Officer Main View\n\
------------------------\n\
[1] Create Event Request \n\
[2] Logout\n")

        if key=="1":
            clear()
            print("Please enter folowing details about the Request")
            client_record_number=input("Client record number: ")
            client_name=input("Client_name: ")
            event_type=input("Event_type: ")
            expected_number_attendees=input("Expected number attendees: ")
            expected_budget=input("Expected budget: ")
            start_date=input("Start date: ")
            end_date=input("End date: ")
            priorities=input("Priorities: ")
            status=input("Status: ")

            atributes=[client_record_number, client_name, event_type, expected_number_attendees, \
            expected_budget, start_date, end_date, priorities, status]

            try:eventRequest_control
            except:eventRequest_control=EventRequest_control()
            eventRequest_control.create_eventRequest(atributes)
            
            input("Event request completed! Press enter to continue")
            
        elif key=="2":
            return
    return 