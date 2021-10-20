# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

import database
from clear import clear

class EventRequest():

    def __init__(self,id):
        self.__id=id
    def add_info(self):
        self.__feasibility_review=None
        self.__financial_review=None
        self.__assigned2="SCSO"

        clear()
        print("Please enter folowing details about the Request")
        self.__client_record_number=input("Client record number: ")
        self.__client_name=input("Client_name: ")
        self.__event_type=input("Event_type: ")
        self.__expected_number_attendees=input("Expected number attendees: ")
        self.__expected_budget=input("Expected budget: ")
        self.__start_date=input("Start date: ")
        self.__end_date=input("End date: ")
        self.__priorities=input("Priorities: ")
        self.__status=input("Status: ")
        input("Event request completed! Press enter to continue")

    def add_info_test(self, atributes):
        self.__assigned2="SCSO"
        self.__client_record_number=atributes[0]
        self.__client_name=atributes[1]
        self.__event_type=atributes[2]
        self.__expected_number_attendees=atributes[3]
        self.__expected_budget=atributes[4]
        self.__start_date=atributes[5]
        self.__end_date=atributes[6]
        self.__priorities=atributes[7]
        self.__status=atributes[8]

    def get_id(self):return self.__id
    def get_name(self):return self.__id
    def get_feasabilty_review(self): return self.__feasibility_review
    def get_assigned2(self):return self.__assigned2

class EventRequest_control():
    def create_eventRequest(self):
        e=EventRequest(database.id_counter.get_new())
        e.add_info()
        database.eventRequest_List.append(e)

    def create_eventRequest_test(self,atributes):
        e=EventRequest(database.id_counter.get_new())
        e.add_info_test(atributes)
        database.eventRequest_List.append(e)
        #database.eventRequest_List.append(EventRequest(database.id_counter.get_new()).add_info_test(atributes))

    def show_event_request_for_user(self):
        clear()
        print("All event requests that are waiting on review")
        print(*[req.get_id() for req in database.eventRequest_List if req and req.get_assigned2()==database.currentUser.position])
        input("Press enter to continue")

    def create_eventRequest_test(self,atributes):
        e=EventRequest(database.id_counter.get_new())
        e.add_info_test(atributes)
        database.eventRequest_List.append(e)
        #database.eventRequest_List.append(EventRequest(database.id_counter.get_new()).add_info_test(atributes))