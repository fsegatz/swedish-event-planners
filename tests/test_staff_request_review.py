import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.user import User_Control
from models.staffrequest import *
import database
from ui.hrtmView import *


def main():
    database.initialize()
    user_Control = User_Control()
    user_Control.fill_user_database()   

    atributes=["id 192", "Decoration" , "40 000" , "Need to buy new chandalier" , "Plz u owe me one", "Opened"]

    
    req1=StaffRequest(database.id_counter.get_new(),atributes)
    req2=StaffRequest(database.id_counter.get_new(),atributes)
    req3=StaffRequest(database.id_counter.get_new(),atributes)

    database.staffRequest_List.append(req1)
    database.staffRequest_List.append(req2)
    database.staffRequest_List.append(req3)

    HumanResourceTeamMemberView() 


main()