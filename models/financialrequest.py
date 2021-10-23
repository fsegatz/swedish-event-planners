import database
from clear import clear

class FinancialRequest:
    def __init__(self, id, atributes):
        self.__id=id
        self.__event_reference=atributes[0]
        self.__requesting_department=atributes[1]
        self.__required_amount=atributes[2]
        self.__reason=atributes[3]
        self.__comment=atributes[4]
        self.__status=atributes[5]
        self.__review=""

    def set_review(self, review): self.__review = review

    def get_status(self): return self.__status
    def get_id(self):return self.__id

    def get_info_as_str(self):
        return "["+ self.__id +  \
                "] | Event reference: " + self.__event_reference+\
                " | Requesting department: " + self.__requesting_department +\
                " | Required amount: " + self.__required_amount + \
                " | Reason: " + self.__reason + \
                " | Comment: " + self.__comment + \
                " | Status: " + self.__status + \
                " | Review: " + self.__review + \
                " |\n"


class FinancialRequest_Control:
    def create_financial_request(self, atributes):
        e=FinancialRequest(id=database.id_counter.get_new(), atributes=atributes)
        database.financialRequest_List.append(e)

    def get_financial_request_from_id(self,id): return [req for req in database.financialRequest_List if req and req.get_id()==id][0]

    def get_str_financial_request_from_id(self, id): return [req.get_info_as_str() for req in database.financialRequest_List if req and req.get_id()==id][0]
    def get_str_financial_requests(self): return [req.get_info_as_str() + "\n" for req in database.financialRequest_List if req and req.get_status()!="Archived"]
    def get_id_of_financial_request_for_user(self): return [req.get_id() for req in database.financialRequest_List if req]
    
    def add_review(self, id, review): 
        [req for req in database.financialRequest_List if req and req.get_id()==id][0]
        request=self.get_financial_request_from_id(id)
        request.set_review(review)
        # if database.currentUser.position=="SCSO":
        #     request.set_feasabilty_review(review)
        #     request.set_assigned2("FM")
        
        # elif database.currentUser.position=="FM":
        #     request.set_financial_review(review)
        #     request.set_assigned2("AM")