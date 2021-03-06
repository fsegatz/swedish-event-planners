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

    def add_info(self, atributes, assigned2, status, feasibility_review, financial_review):
        self.__assigned2=assigned2
        self.__feasibility_review=feasibility_review
        self.__financial_review=financial_review
        self.__status=status

        self.__client_record_number=atributes[0]
        self.__client_name=atributes[1]
        self.__event_type=atributes[2]
        self.__expected_number_attendees=atributes[3]
        self.__expected_budget=atributes[4]
        self.__start_date=atributes[5]
        self.__end_date=atributes[6]
        self.__priorities=atributes[7]

    def get_info_as_str(self):
        return "["+ str(self.__id) +  \
                "] | Client record number: " + self.__client_record_number +\
                " | Client name: " + self.__client_name +\
                " | Event type: " + self.__event_type + \
                " | Expected number attendees: " + self.__expected_number_attendees +\
                " | Expected budget: " + self.__expected_budget + \
                " | Start date: " + self.__start_date + \
                " | End date: " + self.__end_date + \
                " | Priorities: " + self.__priorities + \
                " | Status: " + self.__status + \
                " |"
                # " | Feasibility_review: " + self.__feasibility_review + \
                # " | Financial_review: " + self.__financial_review + \

    def get_id(self):return self.__id
    def get_name(self):return self.__id
    def get_status(self): return self.__status
    def get_feasability_review(self): return self.__feasibility_review
    def get_financial_review(self):return self.__financial_review
    def get_assigned2(self):return self.__assigned2
    def get_all_data(self):return [self.__client_record_number, self.__client_name, self.__event_type, self.__expected_number_attendees, \
            self.__expected_budget, self.__start_date, self.__end_date, self.__priorities, self.__assigned2, self.__status, self.__feasibility_review, self.__financial_review]

    def set_feasabilty_review(self, review):self.__feasibility_review=review
    def set_financial_review(self, review):self.__financial_review=review
    def set_assigned2(self, user): self.__assigned2=user
    def set_status(self, status): self.__status=status

class EventRequest_Control():
    def create_event_request(self,atributes, assigned2="SCSO", status="Under review", feasibility_review="", financial_review=""):
        e=EventRequest(database.id_counter.get_new())
        e.add_info(atributes, assigned2, status, feasibility_review, financial_review)
        database.eventRequest_List.append(e)

    def get_event_request_from_id(self,id): return [req for req in database.eventRequest_List if req and req.get_id()==id][0]
    def get_info_for_event_plan(self, id): return [req.get_all_data() for req in database.eventRequest_List if req and req.get_id()==id][0]
    
    def get_finalized_event_request(self): return [req.get_id() for req in database.eventRequest_List if req and req.get_status()=="Finalized"]
    def get_event_request_for_user(self): return [req.get_info_as_str() + "\n" for req in database.eventRequest_List if req and req.get_assigned2()==database.currentUser.position]
    def get_id_of_event_request_for_user(self): return [req.get_id() for req in database.eventRequest_List if req and req.get_assigned2()==database.currentUser.position]


    def get_reviews_from_event_request(self, id):
        for req in database.eventRequest_List:
            if req.get_id()==id:
                info=req.get_info_as_str()
                if database.currentUser.position=="SCSO":info=info + " Feasibility_review: " + req.get_feasability_review() +" |"
                elif database.currentUser.position in ["FM","AM"]:
                    info=info + " Feasibility_review: " + req.get_feasability_review() +\
                        " | Financial_review: " + req.get_financial_review() +" |"
                return info
    
    def add_review(self, id, review): 
        request=self.get_event_request_from_id(id)
        
        if database.currentUser.position=="SCSO":
            request.set_feasabilty_review(review)
            request.set_assigned2("FM")
        
        elif database.currentUser.position=="FM":
            request.set_financial_review(review)
            request.set_assigned2("AM")
        
    def reject_event_request(self, id):
        for i,req in enumerate(database.eventRequest_List):
            if req.get_id()==id: 
                req.set_status("Rejected")
                req.set_assigned2("")
                #database.eventRequest_List.pop(i)
                return

    def finalize_event_request(self, id):
        request=self.get_event_request_from_id(id)
        request.set_status("Finalized")
        request.set_assigned2("")

    def archived_event_request(self, id): 
        for i,req in enumerate(database.eventRequest_List):
            if req.get_id()==id: 
                req.set_status("Archived")
                req.set_assigned2("")
                #database.eventRequest_List.pop(i)
                return