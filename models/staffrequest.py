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
    def set_status(self, status): self.__status = status

    def get_id(self):return self.__id

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

    def get_staff_request_from_id(self,id): return [req for req in database.staffRequest_List if req and req.get_id()==id][0]

    def get_str_staff_request_from_id(self, id): return [req.get_info_as_str() for req in database.staffRequest_List if req and req.get_id()==id][0]
    def get_str_staff_requests(self): return [req.get_info_as_str() + "\n" for req in database.staffRequest_List if req and req.get_status()!="Archived"]
    def get_id_of_staff_request_for_user(self): return [req.get_id() for req in database.staffRequest_List if req]
    
    def add_status(self, id, status): 
        request=self.get_staff_request_from_id(id)
        request.set_status(status)