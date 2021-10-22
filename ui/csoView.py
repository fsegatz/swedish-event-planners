from models.eventRequest import EventRequest_control
from clear import clear

class CustomerServiceOfficerView:
    def __init__(self):
        self.eventRequest_control=EventRequest_control()
        while True:
            key=self.start_view()

            if key=="1":self.create_event_request()
                
            elif key=="2": return

    def start_view(self): 
        clear()
        print("Customer Service Officer Main View")
        print("------------------------")
        print("[1] Create Event Request")
        print("[2] Logout")
        return input()

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


        self.eventRequest_control.create_eventRequest(atributes)
        
        input("Event request completed! Press enter to continue")