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

    def get_status(self): return self.__status

    def get_info_as_str(self):
        return "["+ self.__id +  \
                "] | Contract type: " + self.__contract_type+\
                " | Requesting department: " + self.__requesting_department +\
                " | Years of experience: " + self.__years_of_experience + \
                " | Job title: " + self.__job_title + \
                " | Job description: " + self.__job_description + \
                " | Status: " + self.__status + \
                " |\n"

class StaffRequest_Control:
    def create_staff_request(self, atributes):
        e=StaffRequest(id=database.id_counter.get_new(), atributes=atributes)
        database.staffRequest_List.append(e)

    def get_current_staff_request(self): return [req.get_info_as_str() for req in database.staffRequest_List if req and req.get_status()!="Archived"]