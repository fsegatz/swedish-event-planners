from ui.userView import UserView
from models.eventrequest import EventRequest_Control
from clear import clear

class CustomerServiceOfficerView(UserView):
    def __init__(self):
        self.eventRequest_Control = EventRequest_Control()
        while True:
            clear()
            self.print_username()
            print("Customer Service Officer Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Create Event Request")
            
            key = input()
            if key=="0": break
            elif key=="1":self.create_event_request()
        return
            
            
    def create_event_request(self):
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

        atributes=[client_record_number, client_name, event_type, expected_number_attendees, \
        expected_budget, start_date, end_date, priorities]

        self.eventRequest_Control.create_event_request(atributes)
        
        input("Event request completed! Press enter to continue")