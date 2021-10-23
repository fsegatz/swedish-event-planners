import database
from clear import clear

class StaffRequest:
    def __init__(self, id, atributes):
        self.__id=id
        self.__contract_type=atributes[0]
        self.__requesting_department=atributes[1]
        self.__years_of_experience=atributes[2]
        self.__job_title=atributes[3]
        self.__job_description=atributes[4]
        self.__status=atributes[5]

class StaffRequest_Control:
    def create_staff_request(self, atributes):
        e=StaffRequest(id=database.id_counter.get_new(), atributes=atributes)
        database.staffRequest_List.append(e)
