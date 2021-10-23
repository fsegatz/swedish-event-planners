import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.staffrequest import *
import database
from ui.hrtmView import *
from ui.pmView import *


def main():
    database.initialize()
    atributes=["Full time", "Decoration" , "4" , "Table fixer" , "fix tables to make them look nice", "opened"]
    
    req1=StaffRequest(database.id_counter.get_new(),atributes)
    req2=StaffRequest(database.id_counter.get_new(),atributes)
    req3=StaffRequest(database.id_counter.get_new(),atributes)

    database.staffRequest_List.append(req1)
    database.staffRequest_List.append(req2)
    database.staffRequest_List.append(req3)

    HumanResourceTeamMemberView().show_current_staff_requests() #start with enter 0


main()