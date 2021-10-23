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

    def get_status(self): return self.__status

    def get_info_as_str(self):
        return "["+ self.__id +  \
                "] | Event reference: " + self.__event_reference+\
                " | Requesting department: " + self.__requesting_department +\
                " | Required amount: " + self.__required_amount + \
                " | Reason: " + self.__reason + \
                " | Comment: " + self.__comment + \
                " | Status: " + self.__status + \
                " |\n"


class FinancialRequest_Control:
    def create_financial_request(self, atributes):
        e=FinancialRequest(id=database.id_counter.get_new(), atributes=atributes)
        database.financialRequest_List.append(e)

    def get_current_financial_request(self): return [req.get_info_as_str() for req in database.financialRequest_List if req and req.get_status()!="Archived"]