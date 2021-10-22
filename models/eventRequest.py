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

    def add_info(self, atributes):
        self.__feasibility_review=None
        self.__financial_review=None
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
    def get_financial_review(self, review):return self.__financial_review
    def get_assigned2(self):return self.__assigned2

    def set_feasabilty_review(self, review):self.__feasibility_review=review
    def set_financial_review(self, review):self.__financial_review=review
    def set_assigned2(self, user): self.__assigned2=user


class EventRequest_control():
    def create_eventRequest(self,atributes):
        e=EventRequest(database.id_counter.get_new())
        e.add_info(atributes)
        database.eventRequest_List.append(e)

    def get_event_request_for_user(self): return [str(req.get_id()) for req in database.eventRequest_List if req and req.get_assigned2()==database.currentUser.position]
    
    def add_review(self, id, review): 
        requests=[req for req in database.eventRequest_List if req.get_id()==int(id)]
        
        if database.currentUser.position=="SCSO":
            requests[0].set_feasabilty_review(review)
            requests[0].set_assigned2("FM")
        
        elif database.currentUser.position=="FM":
            requests[0].set_financial_review(review)
            requests[0].set_assigned2("AM")
        

    def create_eventRequest_test(self,atributes):
        e=EventRequest(database.id_counter.get_new())
        e.add_info(atributes)
        database.eventRequest_List.append(e)

