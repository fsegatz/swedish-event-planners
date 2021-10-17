# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

import database
from clear import clear

class EventRequest():

    def __init__(self):
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

        self.__feasibility_review=None
        self.__financial_review=None

class EventRequest_control():
    def create_eventRequest(self):
        database.eventRequest_List.append(EventRequest())

