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

class FinancialRequest_Control:
    def create_financial_request(self, atributes):
        e=FinancialRequest(id=database.id_counter.get_new(), atributes=atributes)
        database.financialRequest_List.append(e)
